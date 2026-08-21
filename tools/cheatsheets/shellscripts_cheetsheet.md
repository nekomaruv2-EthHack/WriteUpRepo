# Linux Shell Scripting Cheat Sheet

> A practical Bash cheat sheet covering the syntax and patterns required to write production-oriented Linux shell scripts.

---

## Shebang

```bash
#!/usr/bin/env bash
```

Or:

```bash
#!/bin/bash
```

`/usr/bin/env bash` searches for `bash` in `$PATH`, while `/bin/bash` uses a fixed path.

---

## Recommended Script Header

```bash
#!/usr/bin/env bash

set -euo pipefail
```

### `set` options

```bash
set -e      # Exit when a command fails
set -u      # Error on undefined variables
set -o pipefail  # Pipeline fails if any command fails
set -x      # Print commands before executing them (debug)
```

Typical production header:

```bash
set -euo pipefail
```

---

# Variables

## Define Variables

```bash
name="Alice"
count=10
path="/var/log/app.log"
```

Do not put spaces around `=`:

```bash
# Wrong
name = "Alice"

# Correct
name="Alice"
```

---

## Access Variables

```bash
echo "$name"
echo "${name}"
```

Prefer quoting variables:

```bash
echo "$file"
rm "$file"
```

Instead of:

```bash
rm $file
```

---

## Variable Interpolation

```bash
name="Alice"

echo "Hello $name"
echo "Hello ${name}"
```

Use `${}` when concatenating:

```bash
file="log"

echo "${file}.txt"
```

---

## Command Substitution

```bash
current_date=$(date)
hostname=$(hostname)
user_count=$(who | wc -l)
```

Avoid legacy backticks:

```bash
# Avoid
current_date=`date`
```

---

## Arithmetic

```bash
count=10

((count++))
((count += 5))
((count = count * 2))
```

Arithmetic expansion:

```bash
result=$((10 + 5))
```

Example:

```bash
a=10
b=20

sum=$((a + b))
```

---

# Special Variables

```bash
$0      # Script name
$1      # First argument
$2      # Second argument
$#      # Number of arguments
$@      # All arguments
$*      # All arguments
$?      # Exit status of previous command
$$      # Current shell PID
$!      # PID of last background command
```

Example:

```bash
echo "Script: $0"
echo "First argument: $1"
echo "Argument count: $#"
```

---

## `$@` vs `$*`

Prefer:

```bash
"$@"
```

It preserves arguments individually.

Example:

```bash
for arg in "$@"; do
    echo "$arg"
done
```

---

# Default Values

Use parameter expansion.

```bash
${variable:-default}
```

Example:

```bash
name=${USER_NAME:-guest}
```

Meaning:

```text
Use USER_NAME if it exists and is not empty.
Otherwise use "guest".
```

Assign default value:

```bash
${variable:=default}
```

Error if undefined:

```bash
${variable:?error message}
```

Example:

```bash
API_KEY=${API_KEY:?API_KEY is required}
```

Use alternative value:

```bash
${variable:+value}
```

---

# String Operations

## String Length

```bash
text="hello"

echo "${#text}"
```

Output:

```text
5
```

---

## Substring

```bash
text="abcdef"

echo "${text:0:3}"
```

Output:

```text
abc
```

---

## Remove Prefix

```bash
file="/tmp/test.txt"

echo "${file#/tmp/}"
```

Output:

```text
test.txt
```

---

## Remove Suffix

```bash
file="test.tar.gz"

echo "${file%.gz}"
```

Output:

```text
test.tar
```

---

## Replace String

Replace first occurrence:

```bash
text="hello world"

echo "${text/world/linux}"
```

Replace all occurrences:

```bash
echo "${text//o/O}"
```

---

# Quoting

Shell quoting is extremely important.

## Double Quotes

Variables and command substitutions are expanded.

```bash
echo "$HOME"
echo "$(date)"
```

---

## Single Quotes

Nothing is expanded.

```bash
echo '$HOME'
```

Output:

```text
$HOME
```

---

## Escaping

```bash
echo "Price: \$100"
```

---

# Conditionals

## Basic `if`

```bash
if command; then
    echo "success"
fi
```

Example:

```bash
if ping -c 1 google.com >/dev/null 2>&1; then
    echo "Network available"
fi
```

---

## `if / else`

```bash
if condition; then
    command
else
    command
fi
```

---

## `if / elif / else`

```bash
if condition1; then
    command
elif condition2; then
    command
else
    command
fi
```

---

# Test Expressions

Prefer Bash's:

```bash
[[ ... ]]
```

Instead of the older:

```bash
[ ... ]
```

Example:

```bash
if [[ "$name" == "Alice" ]]; then
    echo "Hello Alice"
fi
```

---

# String Comparisons

```bash
[[ "$a" == "$b" ]]
[[ "$a" != "$b" ]]

[[ -z "$a" ]]     # Empty string
[[ -n "$a" ]]     # Non-empty string
```

Pattern matching:

```bash
if [[ "$file" == *.log ]]; then
    echo "Log file"
fi
```

Regex matching:

```bash
if [[ "$value" =~ ^[0-9]+$ ]]; then
    echo "Number"
fi
```

---

# Numeric Comparisons

Inside `[[ ]]`:

```bash
[[ "$a" -eq "$b" ]]
[[ "$a" -ne "$b" ]]
[[ "$a" -gt "$b" ]]
[[ "$a" -ge "$b" ]]
[[ "$a" -lt "$b" ]]
[[ "$a" -le "$b" ]]
```

With arithmetic syntax:

```bash
if (( a > b )); then
    echo "a is greater"
fi
```

For Bash, arithmetic syntax is often cleaner:

```bash
(( a == b ))
(( a != b ))
(( a > b ))
(( a >= b ))
(( a < b ))
(( a <= b ))
```

---

# File Tests

```bash
[[ -e "$file" ]]   # Exists
[[ -f "$file" ]]   # Regular file
[[ -d "$file" ]]   # Directory
[[ -L "$file" ]]   # Symbolic link

[[ -r "$file" ]]   # Readable
[[ -w "$file" ]]   # Writable
[[ -x "$file" ]]   # Executable

[[ -s "$file" ]]   # File exists and is not empty
```

Example:

```bash
if [[ -f "$config" ]]; then
    echo "Config exists"
fi
```

---

# Logical Operators

```bash
[[ condition1 && condition2 ]]
[[ condition1 || condition2 ]]
[[ ! condition ]]
```

Example:

```bash
if [[ -f "$file" && -r "$file" ]]; then
    cat "$file"
fi
```

---

# Short-Circuit Execution

Run second command only if first succeeds:

```bash
command1 && command2
```

Example:

```bash
mkdir backup && cp file.txt backup/
```

Run second command only if first fails:

```bash
command1 || command2
```

Example:

```bash
ping server || echo "Server unreachable"
```

---

# Case Statement

```bash
case "$value" in
    pattern1)
        command
        ;;
    pattern2)
        command
        ;;
    *)
        command
        ;;
esac
```

Example:

```bash
case "$1" in
    start)
        echo "Starting..."
        ;;
    stop)
        echo "Stopping..."
        ;;
    restart)
        echo "Restarting..."
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
        exit 1
        ;;
esac
```

Multiple patterns:

```bash
case "$answer" in
    y|Y|yes|YES)
        echo "Yes"
        ;;
esac
```

---

# For Loops

## Iterate Over Values

```bash
for item in one two three; do
    echo "$item"
done
```

---

## Iterate Over Arguments

```bash
for arg in "$@"; do
    echo "$arg"
done
```

---

## Iterate Over Files

```bash
for file in *.log; do
    echo "$file"
done
```

---

## C-Style Loop

```bash
for ((i = 0; i < 10; i++)); do
    echo "$i"
done
```

---

## Sequence

```bash
for i in {1..10}; do
    echo "$i"
done
```

Or:

```bash
for i in $(seq 1 10); do
    echo "$i"
done
```

Prefer Bash brace expansion when the range is static.

---

# While Loops

```bash
while condition; do
    command
done
```

Example:

```bash
count=0

while (( count < 5 )); do
    echo "$count"
    ((count++))
done
```

---

## Infinite Loop

```bash
while true; do
    command
done
```

Or:

```bash
while :; do
    command
done
```

---

# Until Loop

Runs until the condition becomes true.

```bash
until condition; do
    command
done
```

Example:

```bash
until ping -c 1 server >/dev/null 2>&1; do
    sleep 1
done
```

---

# `break` and `continue`

```bash
for i in {1..10}; do
    if (( i == 5 )); then
        break
    fi
done
```

Skip current iteration:

```bash
for i in {1..10}; do
    if (( i == 5 )); then
        continue
    fi

    echo "$i"
done
```

---

# Functions

## Define Function

```bash
function_name() {
    command
}
```

Example:

```bash
hello() {
    echo "Hello"
}
```

Call:

```bash
hello
```

---

## Function Arguments

```bash
greet() {
    local name="$1"

    echo "Hello $name"
}

greet "Alice"
```

Inside a function:

```bash
$1
$2
$#
$@
```

refer to the function arguments.

---

# Local Variables

Use `local` inside functions.

```bash
example() {
    local name="Alice"
    local count=10
}
```

This prevents accidentally modifying global variables.

---

# Function Return Values

Functions return an **exit status**, not arbitrary strings.

```bash
check_file() {
    if [[ -f "$1" ]]; then
        return 0
    fi

    return 1
}
```

Usage:

```bash
if check_file "/tmp/test"; then
    echo "File exists"
fi
```

To return data, print it:

```bash
get_hostname() {
    hostname
}

host=$(get_hostname)
```

---

# Exit Status

Linux commands normally return:

```text
0     Success
1-255 Failure / special status
```

Check previous command:

```bash
command

echo "$?"
```

Better:

```bash
if command; then
    echo "success"
else
    echo "failed"
fi
```

---

# Exit Script

```bash
exit 0
```

Failure:

```bash
exit 1
```

Example:

```bash
if [[ ! -f "$config" ]]; then
    echo "Config file not found" >&2
    exit 1
fi
```

---

# Arrays

## Indexed Arrays

```bash
servers=("web01" "web02" "db01")
```

Access:

```bash
echo "${servers[0]}"
```

All elements:

```bash
echo "${servers[@]}"
```

Length:

```bash
echo "${#servers[@]}"
```

Iterate:

```bash
for server in "${servers[@]}"; do
    echo "$server"
done
```

Add element:

```bash
servers+=("web03")
```

---

# Associative Arrays

Requires Bash 4+.

```bash
declare -A ports

ports[http]=80
ports[https]=443
ports[ssh]=22
```

Access:

```bash
echo "${ports[ssh]}"
```

Iterate:

```bash
for service in "${!ports[@]}"; do
    echo "$service -> ${ports[$service]}"
done
```

---

# Reading User Input

```bash
read name
```

With prompt:

```bash
read -r -p "Name: " name
```

Always prefer `-r` unless backslash interpretation is required.

Read password silently:

```bash
read -r -s -p "Password: " password
echo
```

---

# Read File Line by Line

Recommended pattern:

```bash
while IFS= read -r line; do
    echo "$line"
done < file.txt
```

Preserves whitespace and backslashes.

---

# Internal Field Separator (`IFS`)

Split strings:

```bash
data="alice:admin:/home/alice"

IFS=':' read -r user role home <<< "$data"
```

Example:

```bash
echo "$user"
echo "$role"
echo "$home"
```

---

# Here String

Pass a string to stdin:

```bash
grep "hello" <<< "$text"
```

---

# Here Document

```bash
cat <<EOF
Hello
World
EOF
```

Variables are expanded:

```bash
name="Alice"

cat <<EOF
Hello $name
EOF
```

Disable expansion:

```bash
cat <<'EOF'
$HOME
$(date)
EOF
```

---

# Redirection

## stdout

Overwrite file:

```bash
command > output.txt
```

Append:

```bash
command >> output.txt
```

---

## stderr

```bash
command 2> error.log
```

Append:

```bash
command 2>> error.log
```

---

## stdout and stderr

```bash
command > output.log 2>&1
```

Bash shorthand:

```bash
command &> output.log
```

Append:

```bash
command &>> output.log
```

---

## Discard Output

```bash
command >/dev/null
```

stdout and stderr:

```bash
command >/dev/null 2>&1
```

---

# File Descriptors

Standard descriptors:

```text
0 = stdin
1 = stdout
2 = stderr
```

Example:

```bash
echo "normal output" >&1
echo "error output" >&2
```

---

# Pipes

```bash
command1 | command2
```

Example:

```bash
ps aux | grep nginx
```

Multiple commands:

```bash
cat file.txt \
    | grep error \
    | sort \
    | uniq
```

With `set -o pipefail`, pipeline failure is detected correctly.

---

# Process Substitution

Useful when a command expects a filename.

```bash
diff <(command1) <(command2)
```

Example:

```bash
diff <(sort file1.txt) <(sort file2.txt)
```

---

# Background Processes

Run in background:

```bash
command &
```

Get PID:

```bash
pid=$!
```

Wait for it:

```bash
wait "$pid"
```

Example:

```bash
sleep 10 &
pid=$!

echo "PID: $pid"

wait "$pid"
```

---

# Multiple Background Jobs

```bash
pids=()

command1 &
pids+=("$!")

command2 &
pids+=("$!")

for pid in "${pids[@]}"; do
    wait "$pid"
done
```

---

# Grouping Commands

## Subshell

```bash
(
    cd /tmp
    command
)
```

Changes such as `cd` do not affect the parent shell.

---

## Current Shell

```bash
{
    command1
    command2
}
```

Important:

```bash
{
    echo "hello"
    echo "world"
} > output.txt
```

---

# Script Arguments

```bash
./script.sh arg1 arg2
```

Access:

```bash
$1
$2
```

---

# `shift`

Remove the first positional argument:

```bash
while (($# > 0)); do
    echo "$1"
    shift
done
```

---

# Argument Parsing with `getopts`

```bash
usage() {
    echo "Usage: $0 [-v] [-f file]"
}
```

Example:

```bash
verbose=false
file=""

while getopts ":vf:" opt; do
    case "$opt" in
        v)
            verbose=true
            ;;
        f)
            file="$OPTARG"
            ;;
        :)
            echo "Option -$OPTARG requires an argument." >&2
            exit 1
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            usage
            exit 1
            ;;
    esac
done

shift $((OPTIND - 1))
```

---

# Long Options

`getopts` only directly supports short options.

A common manual pattern:

```bash
while (($# > 0)); do
    case "$1" in
        --verbose)
            verbose=true
            shift
            ;;

        --file)
            file="$2"
            shift 2
            ;;

        --file=*)
            file="${1#*=}"
            shift
            ;;

        --)
            shift
            break
            ;;

        *)
            echo "Unknown argument: $1" >&2
            exit 1
            ;;
    esac
done
```

---

# Environment Variables

Read:

```bash
echo "$PATH"
echo "$HOME"
```

Export:

```bash
export APP_ENV="production"
```

For one command only:

```bash
APP_ENV=production ./app
```

---

# Source Another Script

```bash
source config.sh
```

Equivalent:

```bash
. config.sh
```

Variables and functions are loaded into the current shell.

---

# Check Whether a Command Exists

```bash
if command -v curl >/dev/null 2>&1; then
    echo "curl is installed"
fi
```

Reusable helper:

```bash
require_command() {
    if ! command -v "$1" >/dev/null 2>&1; then
        echo "Required command not found: $1" >&2
        exit 1
    fi
}
```

---

# Path Handling

Get script directory:

```bash
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
```

Example:

```bash
config="${SCRIPT_DIR}/config/app.conf"
```

This avoids depending on the caller's current directory.

---

# Temporary Files

Use `mktemp`.

```bash
tmpfile=$(mktemp)
```

Temporary directory:

```bash
tmpdir=$(mktemp -d)
```

Cleanup:

```bash
trap 'rm -rf "$tmpdir"' EXIT
```

---

# `trap`

Execute commands when signals or script events occur.

```bash
trap 'echo "Exiting"' EXIT
```

Common signals:

```bash
trap 'cleanup' EXIT
trap 'cleanup; exit 130' INT
trap 'cleanup; exit 143' TERM
```

Example:

```bash
tmpdir=$(mktemp -d)

cleanup() {
    rm -rf "$tmpdir"
}

trap cleanup EXIT
```

---

# Error Handling

Basic helper:

```bash
die() {
    echo "ERROR: $*" >&2
    exit 1
}
```

Usage:

```bash
[[ -f "$config" ]] || die "Config not found: $config"
```

---

# Logging

Simple logging functions:

```bash
log() {
    printf '[INFO] %s\n' "$*"
}

warn() {
    printf '[WARN] %s\n' "$*" >&2
}

error() {
    printf '[ERROR] %s\n' "$*" >&2
}
```

With timestamps:

```bash
log() {
    printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*"
}
```

---

# `printf` vs `echo`

Prefer `printf` in scripts.

```bash
printf '%s\n' "$value"
```

Formatted output:

```bash
printf 'Name: %-10s Age: %d\n' "$name" "$age"
```

`echo` behavior can vary between implementations.

---

# `grep`

Find matching lines:

```bash
grep "error" file.log
```

Ignore case:

```bash
grep -i "error" file.log
```

Regex:

```bash
grep -E 'error|warning' file.log
```

Only matching text:

```bash
grep -oE '[0-9]+'
```

Quiet mode:

```bash
if grep -q "error" file.log; then
    echo "Error found"
fi
```

---

# `sed`

Replace:

```bash
sed 's/foo/bar/' file
```

Replace all occurrences:

```bash
sed 's/foo/bar/g' file
```

Edit file in place:

```bash
sed -i 's/foo/bar/g' file
```

Print specific lines:

```bash
sed -n '10,20p' file
```

---

# `awk`

Print column:

```bash
awk '{print $1}' file
```

Custom delimiter:

```bash
awk -F: '{print $1}' /etc/passwd
```

Conditional:

```bash
awk '$3 > 1000 {print $1}' file
```

Pass shell variable:

```bash
awk -v value="$value" '$1 == value {print}' file
```

---

# `cut`

Split by delimiter:

```bash
cut -d: -f1 /etc/passwd
```

Character range:

```bash
cut -c1-10 file
```

---

# `sort`

```bash
sort file
```

Numeric:

```bash
sort -n file
```

Reverse:

```bash
sort -r file
```

Unique:

```bash
sort -u file
```

---

# `uniq`

```bash
sort file | uniq
```

Count occurrences:

```bash
sort file | uniq -c
```

---

# `tr`

Replace characters:

```bash
echo "hello" | tr 'a-z' 'A-Z'
```

Delete characters:

```bash
echo "hello" | tr -d 'l'
```

---

# `xargs`

Convert stdin into command arguments:

```bash
printf '%s\n' *.log | xargs rm
```

Safer filename handling:

```bash
find . -type f -print0 | xargs -0 command
```

When possible, `find -exec` is often safer:

```bash
find . -type f -exec command {} +
```

---

# `find`

Find files:

```bash
find /var/log -type f
```

By name:

```bash
find . -name "*.log"
```

Modified in last day:

```bash
find . -type f -mtime -1
```

Execute command:

```bash
find . -type f -name "*.tmp" -exec rm -- {} +
```

---

# `basename` and `dirname`

```bash
path="/var/log/app.log"

basename "$path"
dirname "$path"
```

Output:

```text
app.log
/var/log
```

---

# File Manipulation

```bash
cp source destination
mv source destination
rm file
mkdir directory
mkdir -p parent/child
touch file
ln -s target link
```

Use `--` before user-controlled filenames where supported:

```bash
rm -- "$file"
```

This prevents filenames such as:

```text
-rf
```

from being interpreted as options.

---

# Permissions

```bash
chmod +x script.sh
chmod 755 script.sh
```

Change owner:

```bash
chown user:group file
```

---

# Networking

## `curl`

GET:

```bash
curl https://example.com
```

Fail on HTTP errors:

```bash
curl -f https://example.com
```

Recommended for scripts:

```bash
curl -fsSL https://example.com
```

POST JSON:

```bash
curl -fsS \
    -X POST \
    -H 'Content-Type: application/json' \
    -d '{"name":"Alice"}' \
    https://example.com/api
```

---

## `wget`

```bash
wget https://example.com/file.tar.gz
```

Quiet:

```bash
wget -q URL
```

---

# JSON with `jq`

Read property:

```bash
jq '.name' file.json
```

Raw string:

```bash
jq -r '.name' file.json
```

Pipe:

```bash
curl -fsS https://example.com/api | jq -r '.data.id'
```

Pass shell variables:

```bash
jq --arg name "$name" '.name = $name' file.json
```

---

# SSH

Execute remote command:

```bash
ssh user@server 'hostname'
```

Pass variables carefully:

```bash
ssh user@server "echo '$value'"
```

For complex remote scripts:

```bash
ssh user@server 'bash -s' <<'EOF'
hostname
uptime
df -h
EOF
```

---

# `sudo`

Run command as root:

```bash
sudo command
```

Check whether running as root:

```bash
if (( EUID != 0 )); then
    echo "Run this script as root." >&2
    exit 1
fi
```

---

# Signals

Common signals:

```text
SIGINT   2    Ctrl+C
SIGTERM  15   Termination request
SIGKILL  9    Forced termination
SIGHUP   1    Hangup / reload
```

Send signal:

```bash
kill -TERM "$pid"
```

---

# Job Control

Background:

```bash
command &
```

Wait:

```bash
wait
```

Wait for specific PID:

```bash
wait "$pid"
```

---

# Locking

Prevent multiple script instances with `flock`.

```bash
exec 200>/var/lock/my-script.lock

flock -n 200 || {
    echo "Script already running"
    exit 1
}
```

Another pattern:

```bash
flock -n /tmp/my-script.lock ./script.sh
```

---

# Checking Lock / PID Files

PID file pattern:

```bash
pidfile="/var/run/my-script.pid"

if [[ -f "$pidfile" ]]; then
    pid=$(<"$pidfile")

    if kill -0 "$pid" 2>/dev/null; then
        echo "Already running"
        exit 1
    fi
fi

echo "$$" > "$pidfile"
trap 'rm -f "$pidfile"' EXIT
```

When available, prefer `flock`.

---

# Reading a File Directly

Instead of:

```bash
value=$(cat file.txt)
```

Bash can use:

```bash
value=$(<file.txt)
```

---

# Null Command `:`

The `:` command does nothing and returns success.

```bash
:
```

Useful for defaults:

```bash
: "${CONFIG:=config.ini}"
```

Or infinite loops:

```bash
while :; do
    command
done
```

---

# `true` and `false`

```bash
true
false
```

They return exit codes:

```text
true  -> 0
false -> 1
```

Example:

```bash
if true; then
    echo "Executed"
fi
```

---

# Brace Expansion

```bash
echo file{1..5}.txt
```

Output:

```text
file1.txt file2.txt file3.txt file4.txt file5.txt
```

Multiple values:

```bash
mkdir -p /opt/app/{bin,config,logs}
```

---

# Globbing

```bash
*.txt
?.txt
[a-z].txt
```

Examples:

```bash
for file in *.log; do
    echo "$file"
done
```

Bash extended globbing:

```bash
shopt -s extglob
```

Examples:

```bash
@(foo|bar)
!(foo)
+(pattern)
*(pattern)
?(pattern)
```

---

# Shell Options

View options:

```bash
shopt
```

Useful options:

```bash
shopt -s nullglob
```

Without `nullglob`:

```bash
files=(*.does-not-exist)
```

may contain the literal pattern.

With `nullglob` it expands to nothing.

Useful:

```bash
shopt -s nullglob
shopt -s globstar
```

`globstar` enables:

```bash
**/*.log
```

recursive matching.

---

# Regex Matching

```bash
value="server123"

if [[ "$value" =~ ^server[0-9]+$ ]]; then
    echo "Match"
fi
```

Captured groups:

```bash
value="user:123"

if [[ "$value" =~ ^([^:]+):([0-9]+)$ ]]; then
    user="${BASH_REMATCH[1]}"
    id="${BASH_REMATCH[2]}"
fi
```

---

# Debugging

Enable command tracing:

```bash
set -x
```

Disable:

```bash
set +x
```

Run script:

```bash
bash -x script.sh
```

Syntax check without execution:

```bash
bash -n script.sh
```

---

# Debug Information

Useful variables:

```bash
${BASH_SOURCE[0]}
${FUNCNAME[0]}
${LINENO}
```

Example:

```bash
debug() {
    printf '[DEBUG] %s:%s %s\n' \
        "${BASH_SOURCE[1]}" \
        "${BASH_LINENO[0]}" \
        "$*"
}
```

---

# Error Trap

```bash
trap 'echo "Error on line $LINENO" >&2' ERR
```

More useful pattern:

```bash
error_handler() {
    local exit_code=$?
    local line=$1

    echo "ERROR: line $line exited with status $exit_code" >&2
    exit "$exit_code"
}

trap 'error_handler $LINENO' ERR
```

---

# ShellCheck

Use ShellCheck to detect common shell scripting mistakes.

```bash
shellcheck script.sh
```

Typical issues detected:

```text
Unquoted variables
Incorrect array handling
Broken command substitutions
Unsafe word splitting
Unused variables
Invalid tests
```

---

# Common Safe Patterns

## Quote Variables

Prefer:

```bash
rm -- "$file"
```

Avoid:

```bash
rm $file
```

---

## Preserve Arguments

Prefer:

```bash
command "$@"
```

Avoid:

```bash
command $@
```

---

## Read Lines Safely

Prefer:

```bash
while IFS= read -r line; do
    ...
done < "$file"
```

---

## Avoid Parsing `ls`

Do not:

```bash
for file in $(ls *.txt); do
    ...
done
```

Use globbing:

```bash
for file in *.txt; do
    ...
done
```

Or `find` when recursive processing is required.

---

## Avoid Useless `cat`

Instead of:

```bash
cat file.txt | grep error
```

Use:

```bash
grep error file.txt
```

---

## Avoid Checking `$?` Separately

Instead of:

```bash
command

if [[ $? -eq 0 ]]; then
    echo "success"
fi
```

Prefer:

```bash
if command; then
    echo "success"
fi
```

---

# Common Script Structure

```bash
#!/usr/bin/env bash

set -euo pipefail

readonly SCRIPT_NAME="${0##*/}"
readonly SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

log() {
    printf '[INFO] %s\n' "$*"
}

error() {
    printf '[ERROR] %s\n' "$*" >&2
}

die() {
    error "$@"
    exit 1
}

usage() {
    cat <<EOF
Usage:
  $SCRIPT_NAME [options]

Options:
  -h, --help        Show this help
  -v, --verbose     Enable verbose output
EOF
}

cleanup() {
    :
}

main() {
    local verbose=false

    while (($# > 0)); do
        case "$1" in
            -h|--help)
                usage
                return 0
                ;;

            -v|--verbose)
                verbose=true
                shift
                ;;

            --)
                shift
                break
                ;;

            *)
                die "Unknown argument: $1"
                ;;
        esac
    done

    log "Starting $SCRIPT_NAME"

    if "$verbose"; then
        log "Verbose mode enabled"
    fi
}

trap cleanup EXIT

main "$@"
```

---

# Production Script Template

```bash
#!/usr/bin/env bash

set -Eeuo pipefail

readonly SCRIPT_NAME="${0##*/}"
readonly SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

log() {
    printf '[%s] [INFO] %s\n' \
        "$(date '+%Y-%m-%d %H:%M:%S')" \
        "$*"
}

warn() {
    printf '[%s] [WARN] %s\n' \
        "$(date '+%Y-%m-%d %H:%M:%S')" \
        "$*" >&2
}

error() {
    printf '[%s] [ERROR] %s\n' \
        "$(date '+%Y-%m-%d %H:%M:%S')" \
        "$*" >&2
}

die() {
    error "$@"
    exit 1
}

cleanup() {
    :
}

on_error() {
    local exit_code=$?
    local line="$1"

    error "Command failed at line $line with exit code $exit_code"

    exit "$exit_code"
}

require_command() {
    command -v "$1" >/dev/null 2>&1 ||
        die "Required command not found: $1"
}

main() {
    require_command curl

    log "Starting $SCRIPT_NAME"

    # Application logic here

    log "Completed successfully"
}

trap 'on_error $LINENO' ERR
trap cleanup EXIT

main "$@"
```

---

# Bash vs POSIX `sh`

Bash-specific features include:

```bash
[[ ... ]]
(( ... ))
arrays
associative arrays
${BASH_SOURCE}
process substitution <(...)
=~
shopt
```

For maximum portability:

```bash
#!/bin/sh
```

requires avoiding many Bash-specific features.

For modern Linux administration and internal tooling, Bash is usually more practical:

```bash
#!/usr/bin/env bash
```

---

# Quick Reference

```bash
# Variable
name="Alice"
echo "$name"

# Command substitution
date=$(date)

# Arithmetic
result=$((a + b))

# Condition
if [[ "$a" == "$b" ]]; then
    ...
fi

# Numeric condition
if (( count > 10 )); then
    ...
fi

# File check
[[ -f "$file" ]]

# Loop
for item in "${items[@]}"; do
    ...
done

# While
while condition; do
    ...
done

# Function
function_name() {
    local value="$1"
}

# Array
items=("a" "b" "c")

# Arguments
"$1"
"$@"
"$#"

# Default value
value=${VALUE:-default}

# Error
echo "error" >&2

# Exit
exit 1

# Pipe
command1 | command2

# Redirect
command > file 2>&1

# Background
command &
pid=$!
wait "$pid"

# Cleanup
trap cleanup EXIT

# Check command
command -v curl >/dev/null 2>&1

# Script directory
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
```

---

# Recommended Practices

```text
1. Use Bash explicitly when using Bash syntax.
2. Start non-trivial scripts with `set -euo pipefail`.
3. Quote variable expansions unless word splitting is intentional.
4. Prefer `[[ ... ]]` for Bash conditions.
5. Prefer `(( ... ))` for arithmetic.
6. Use arrays instead of space-separated strings.
7. Use `local` variables inside functions.
8. Use functions to separate script responsibilities.
9. Use exit codes consistently.
10. Write errors to stderr.
11. Use `mktemp` for temporary files.
12. Use `trap` for cleanup.
13. Use `command -v` to check dependencies.
14. Avoid parsing `ls`.
15. Use `while IFS= read -r` for line-based file processing.
16. Prefer `printf` over `echo` for predictable output.
17. Pass script arguments using `"$@"`.
18. Run `shellcheck` against production scripts.
19. Run `bash -n script.sh` before execution.
20. Treat filenames, arguments, and environment variables as untrusted input.
```
