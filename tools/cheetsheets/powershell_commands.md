# PowerShell Command Cheat Sheet for Linux Users

> Common PowerShell commands mapped to familiar Linux commands.

---

# Navigation

## `pwd` — Show Current Directory

Linux:

```bash
pwd
```

PowerShell:

```powershell
Get-Location
```

Alias:

```powershell
pwd
```

---

## `cd` — Change Directory

Linux:

```bash
cd /var/log
```

PowerShell:

```powershell
Set-Location C:\Windows\Logs
```

Alias:

```powershell
cd C:\Windows\Logs
```

Go to parent directory:

```powershell
cd ..
```

Go to home directory:

```powershell
cd ~
```

---

## List Available Drives

```powershell
Get-PSDrive
```

Example:

```text
Name
----
C
D
Env
Alias
Variable
```

PowerShell paths are not limited to filesystems.

For example:

```powershell
cd Env:
```

allows browsing environment variables like a directory.

---

# Listing Files

## `ls` — List Files and Directories

Linux:

```bash
ls
```

PowerShell:

```powershell
Get-ChildItem
```

Aliases:

```powershell
ls
dir
gci
```

---

## Detailed Listing

Linux:

```bash
ls -l
```

PowerShell:

```powershell
Get-ChildItem | Format-Table
```

Useful properties:

```powershell
Get-ChildItem | Select-Object Name, Length, LastWriteTime
```

---

## Show Hidden Files

Linux:

```bash
ls -a
```

PowerShell:

```powershell
Get-ChildItem -Force
```

Alias:

```powershell
ls -Force
```

---

## List Only Files

```powershell
Get-ChildItem -File
```

---

## List Only Directories

```powershell
Get-ChildItem -Directory
```

---

## Recursive Listing

Linux:

```bash
ls -R
```

PowerShell:

```powershell
Get-ChildItem -Recurse
```

---

# Creating Files and Directories

## `mkdir` — Create Directory

Linux:

```bash
mkdir test
```

PowerShell:

```powershell
New-Item -ItemType Directory -Name test
```

Alias:

```powershell
mkdir test
```

---

## `mkdir -p`

Linux:

```bash
mkdir -p parent/child
```

PowerShell:

```powershell
New-Item -ItemType Directory -Path "parent\child" -Force
```

---

## `touch` — Create Empty File

Linux:

```bash
touch test.txt
```

PowerShell:

```powershell
New-Item -ItemType File test.txt
```

Short form:

```powershell
ni test.txt -ItemType File
```

If the file already exists and you want to update its timestamp:

```powershell
(Get-Item test.txt).LastWriteTime = Get-Date
```

---

# Copying Files

## `cp` — Copy File

Linux:

```bash
cp file.txt backup.txt
```

PowerShell:

```powershell
Copy-Item file.txt backup.txt
```

Aliases:

```powershell
cp
copy
cpi
```

---

## Copy Directory Recursively

Linux:

```bash
cp -r src dst
```

PowerShell:

```powershell
Copy-Item src dst -Recurse
```

Example:

```powershell
Copy-Item .\src .\backup -Recurse
```

---

## Force Overwrite

```powershell
Copy-Item source.txt destination.txt -Force
```

---

# Moving and Renaming

## `mv` — Move File

Linux:

```bash
mv file.txt /tmp/
```

PowerShell:

```powershell
Move-Item file.txt C:\Temp\
```

Aliases:

```powershell
mv
move
mi
```

---

## Rename File

Linux:

```bash
mv old.txt new.txt
```

PowerShell:

```powershell
Rename-Item old.txt new.txt
```

Alias:

```powershell
ren old.txt new.txt
```

---

# Removing Files

## `rm` — Remove File

Linux:

```bash
rm file.txt
```

PowerShell:

```powershell
Remove-Item file.txt
```

Aliases:

```powershell
rm
del
ri
```

---

## `rm -r` — Remove Directory Recursively

Linux:

```bash
rm -r directory
```

PowerShell:

```powershell
Remove-Item directory -Recurse
```

---

## `rm -rf`

Linux:

```bash
rm -rf directory
```

PowerShell:

```powershell
Remove-Item directory -Recurse -Force
```

Be careful:

```powershell
Remove-Item .\something -Recurse -Force
```

can permanently delete files without moving them to the Recycle Bin.

---

# Finding Files

## `find`

Linux:

```bash
find . -name "*.txt"
```

PowerShell:

```powershell
Get-ChildItem -Recurse -Filter "*.txt"
```

Short form:

```powershell
gci -Recurse -Filter "*.txt"
```

---

## Find Files Only

```powershell
Get-ChildItem -Recurse -File
```

---

## Find Directories Only

```powershell
Get-ChildItem -Recurse -Directory
```

---

## Find by File Name

```powershell
Get-ChildItem -Recurse -File |
    Where-Object Name -eq "config.txt"
```

Wildcard:

```powershell
Get-ChildItem -Recurse -File |
    Where-Object Name -like "*.log"
```

---

## Find Files Larger Than 100 MB

Linux:

```bash
find . -size +100M
```

PowerShell:

```powershell
Get-ChildItem -Recurse -File |
    Where-Object Length -gt 100MB
```

PowerShell understands size constants:

```powershell
1KB
1MB
1GB
1TB
```

---

## Find Recently Modified Files

Files modified within the last 24 hours:

```powershell
Get-ChildItem -Recurse -File |
    Where-Object LastWriteTime -gt (Get-Date).AddDays(-1)
```

---

# Reading Files

## `cat`

Linux:

```bash
cat file.txt
```

PowerShell:

```powershell
Get-Content file.txt
```

Aliases:

```powershell
cat
gc
type
```

---

## Read Entire File as One String

Default `Get-Content` returns lines individually.

To get one string:

```powershell
Get-Content file.txt -Raw
```

---

# `head`

Linux:

```bash
head file.txt
```

PowerShell:

```powershell
Get-Content file.txt | Select-Object -First 10
```

Or:

```powershell
Get-Content file.txt -TotalCount 10
```

---

# `tail`

Linux:

```bash
tail file.txt
```

PowerShell:

```powershell
Get-Content file.txt -Tail 10
```

---

## `tail -f`

Linux:

```bash
tail -f app.log
```

PowerShell:

```powershell
Get-Content app.log -Wait
```

Usually:

```powershell
Get-Content app.log -Tail 20 -Wait
```

---

# Writing Files

## `echo > file`

Linux:

```bash
echo "hello" > file.txt
```

PowerShell:

```powershell
"hello" > file.txt
```

Or:

```powershell
Set-Content file.txt "hello"
```

---

## Append

Linux:

```bash
echo "hello" >> file.txt
```

PowerShell:

```powershell
"hello" >> file.txt
```

Or:

```powershell
Add-Content file.txt "hello"
```

---

# Searching Inside Files

## `grep`

Linux:

```bash
grep "error" app.log
```

PowerShell:

```powershell
Select-String "error" app.log
```

---

## Recursive Grep

Linux:

```bash
grep -r "error" .
```

PowerShell:

```powershell
Get-ChildItem -Recurse -File |
    Select-String "error"
```

---

## Case-Sensitive Search

PowerShell string matching is generally case-insensitive by default.

Case-sensitive:

```powershell
Select-String "ERROR" app.log -CaseSensitive
```

---

## Regex Search

```powershell
Select-String "error|warning" app.log
```

`Select-String` uses regular expressions by default.

Literal string:

```powershell
Select-String "hello.world" file.txt -SimpleMatch
```

---

# Filtering

## `grep`-like Object Filtering

One of the most important PowerShell commands:

```powershell
Where-Object
```

Example:

```powershell
Get-ChildItem |
    Where-Object Length -gt 1MB
```

Traditional syntax:

```powershell
Get-ChildItem |
    Where-Object { $_.Length -gt 1MB }
```

Alias:

```powershell
?
```

Example:

```powershell
Get-ChildItem | ? Length -gt 1MB
```

`$_` means:

```text
Current pipeline object
```

---

# Selecting Columns / Properties

Linux often uses:

```bash
awk
cut
```

PowerShell usually uses:

```powershell
Select-Object
```

Example:

```powershell
Get-ChildItem |
    Select-Object Name, Length
```

Output:

```text
Name          Length
----          ------
file.txt        1024
test.log        4096
```

---

## Select First N Items

```powershell
Get-ChildItem |
    Select-Object -First 5
```

---

## Select Last N Items

```powershell
Get-ChildItem |
    Select-Object -Last 5
```

---

# Sorting

## `sort`

Linux:

```bash
sort file.txt
```

PowerShell:

```powershell
Get-Content file.txt |
    Sort-Object
```

For objects:

```powershell
Get-ChildItem |
    Sort-Object Length
```

Descending:

```powershell
Get-ChildItem |
    Sort-Object Length -Descending
```

---

# `uniq`

Linux:

```bash
sort file.txt | uniq
```

PowerShell:

```powershell
Get-Content file.txt |
    Sort-Object -Unique
```

Or:

```powershell
Get-Content file.txt |
    Group-Object
```

---

# Counting

## `wc -l`

Linux:

```bash
wc -l file.txt
```

PowerShell:

```powershell
Get-Content file.txt |
    Measure-Object -Line
```

Simpler:

```powershell
(Get-Content file.txt).Count
```

---

## Count Files

```powershell
(Get-ChildItem -File).Count
```

Recursive:

```powershell
(Get-ChildItem -Recurse -File).Count
```

---

# Disk Usage

## `du`

Linux:

```bash
du -sh directory
```

PowerShell:

```powershell
Get-ChildItem directory -Recurse -File |
    Measure-Object Length -Sum
```

Human-readable MB:

```powershell
$size = (
    Get-ChildItem directory -Recurse -File |
    Measure-Object Length -Sum
).Sum

"{0:N2} MB" -f ($size / 1MB)
```

---

# Disk Space

## `df`

Linux:

```bash
df -h
```

PowerShell:

```powershell
Get-PSDrive -PSProvider FileSystem
```

Example:

```powershell
Get-PSDrive C
```

More detailed Windows disk information:

```powershell
Get-CimInstance Win32_LogicalDisk
```

---

# File Information

## `stat`

Linux:

```bash
stat file.txt
```

PowerShell:

```powershell
Get-Item file.txt
```

Detailed:

```powershell
Get-Item file.txt |
    Format-List *
```

Useful properties:

```powershell
Get-Item file.txt |
    Select-Object Name, Length, CreationTime, LastWriteTime
```

---

# File Type

Linux:

```bash
file example.exe
```

PowerShell does not have a direct built-in equivalent to GNU `file`.

Useful basic information:

```powershell
Get-Item example.exe |
    Format-List *
```

For executable metadata:

```powershell
(Get-Item example.exe).VersionInfo
```

---

# Symbolic Links

## `ln -s`

Linux:

```bash
ln -s target link
```

PowerShell:

```powershell
New-Item -ItemType SymbolicLink -Path link -Target target
```

Example:

```powershell
New-Item `
    -ItemType SymbolicLink `
    -Path .\config-link `
    -Target .\config
```

---

# Paths

## Join Paths

Instead of manually writing:

```powershell
$dir + "\" + $file
```

prefer:

```powershell
Join-Path $dir $file
```

Example:

```powershell
$path = Join-Path "C:\Temp" "test.txt"
```

---

## Resolve Absolute Path

Linux:

```bash
realpath file.txt
```

PowerShell:

```powershell
Resolve-Path file.txt
```

---

## File Name

Linux:

```bash
basename /tmp/test.txt
```

PowerShell:

```powershell
Split-Path "C:\Temp\test.txt" -Leaf
```

Output:

```text
test.txt
```

---

## Parent Directory

Linux:

```bash
dirname /tmp/test.txt
```

PowerShell:

```powershell
Split-Path "C:\Temp\test.txt" -Parent
```

Output:

```text
C:\Temp
```

---

# Wildcards

PowerShell supports familiar wildcards:

```powershell
*.txt
*.log
test?.txt
```

Example:

```powershell
Get-ChildItem *.txt
```

Recursive:

```powershell
Get-ChildItem -Recurse -Filter "*.txt"
```

---

# Check Whether File Exists

Linux:

```bash
test -f file.txt
```

PowerShell:

```powershell
Test-Path file.txt
```

Example:

```powershell
if (Test-Path file.txt) {
    Write-Output "File exists"
}
```

---

## Check Directory

```powershell
Test-Path directory -PathType Container
```

Check file:

```powershell
Test-Path file.txt -PathType Leaf
```

---

# Environment Variables

## List Environment Variables

Linux:

```bash
env
```

PowerShell:

```powershell
Get-ChildItem Env:
```

---

## Read Environment Variable

Linux:

```bash
echo $PATH
```

PowerShell:

```powershell
$env:PATH
```

---

## Set Environment Variable

Linux:

```bash
export APP_ENV=production
```

PowerShell:

```powershell
$env:APP_ENV = "production"
```

This affects the current PowerShell process and child processes.

---

# Command Lookup

## `which`

Linux:

```bash
which python
```

PowerShell:

```powershell
Get-Command python
```

Alias:

```powershell
gcm python
```

Example:

```powershell
Get-Command ssh
```

---

# Clear Screen

Linux:

```bash
clear
```

PowerShell:

```powershell
Clear-Host
```

Aliases:

```powershell
clear
cls
```

---

# Output

## `echo`

Linux:

```bash
echo "hello"
```

PowerShell:

```powershell
Write-Output "hello"
```

Also works:

```powershell
echo "hello"
```

Often simply:

```powershell
"hello"
```

is enough.

---

# Pipeline

Linux:

```bash
ls | grep ".txt"
```

PowerShell:

```powershell
Get-ChildItem |
    Where-Object Name -like "*.txt"
```

Important difference:

```text
Linux pipelines usually pass text.

PowerShell pipelines usually pass objects.
```

For example:

```powershell
Get-ChildItem
```

does not simply output formatted text.

It outputs objects containing properties such as:

```text
Name
Length
CreationTime
LastWriteTime
Attributes
FullName
```

Therefore:

```powershell
Get-ChildItem |
    Where-Object Length -gt 1MB |
    Sort-Object Length -Descending |
    Select-Object Name, Length
```

is roughly conceptually equivalent to combining commands such as:

```bash
find
grep
awk
sort
```

in Linux.

---

# Tee

Linux:

```bash
command | tee output.txt
```

PowerShell:

```powershell
Get-ChildItem |
    Tee-Object -FilePath output.txt
```

---

# Useful File System Examples

## Find All `.log` Files

```powershell
Get-ChildItem -Recurse -File -Filter "*.log"
```

---

## Find Large Files

```powershell
Get-ChildItem -Recurse -File |
    Where-Object Length -gt 100MB |
    Sort-Object Length -Descending
```

---

## Find Files Containing "password"

```powershell
Get-ChildItem -Recurse -File |
    Select-String "password"
```

---

## Find Recently Modified Files

```powershell
Get-ChildItem -Recurse -File |
    Where-Object LastWriteTime -gt (Get-Date).AddHours(-24)
```

---

## Delete All `.tmp` Files

```powershell
Get-ChildItem -Recurse -File -Filter "*.tmp" |
    Remove-Item
```

Preview first:

```powershell
Get-ChildItem -Recurse -File -Filter "*.tmp"
```

Safer simulation:

```powershell
Get-ChildItem -Recurse -File -Filter "*.tmp" |
    Remove-Item -WhatIf
```

`-WhatIf` is extremely useful for destructive PowerShell commands.

---

# Linux → PowerShell Quick Reference

| Linux        | PowerShell                        | Meaning                   |
| ------------ | --------------------------------- | ------------------------- |
| `pwd`        | `Get-Location`                    | Current directory         |
| `cd`         | `Set-Location`                    | Change directory          |
| `ls`         | `Get-ChildItem`                   | List files                |
| `ls -a`      | `Get-ChildItem -Force`            | Include hidden files      |
| `ls -R`      | `Get-ChildItem -Recurse`          | Recursive listing         |
| `mkdir`      | `New-Item -ItemType Directory`    | Create directory          |
| `touch`      | `New-Item -ItemType File`         | Create file               |
| `cp`         | `Copy-Item`                       | Copy                      |
| `cp -r`      | `Copy-Item -Recurse`              | Recursive copy            |
| `mv`         | `Move-Item`                       | Move                      |
| `mv old new` | `Rename-Item`                     | Rename                    |
| `rm`         | `Remove-Item`                     | Delete                    |
| `rm -rf`     | `Remove-Item -Recurse -Force`     | Recursive forced delete   |
| `cat`        | `Get-Content`                     | Read file                 |
| `head`       | `Select-Object -First`            | First lines/items         |
| `tail`       | `Get-Content -Tail`               | Last lines                |
| `tail -f`    | `Get-Content -Wait`               | Follow file               |
| `grep`       | `Select-String`                   | Search text               |
| `find`       | `Get-ChildItem -Recurse`          | Find files                |
| `which`      | `Get-Command`                     | Locate command            |
| `sort`       | `Sort-Object`                     | Sort                      |
| `uniq`       | `Sort-Object -Unique`             | Unique values             |
| `wc`         | `Measure-Object`                  | Count                     |
| `df`         | `Get-PSDrive`                     | Disk space                |
| `du`         | `Measure-Object Length -Sum`      | Directory size            |
| `stat`       | `Get-Item`                        | File metadata             |
| `realpath`   | `Resolve-Path`                    | Absolute path             |
| `basename`   | `Split-Path -Leaf`                | File name                 |
| `dirname`    | `Split-Path -Parent`              | Parent path               |
| `ln -s`      | `New-Item -ItemType SymbolicLink` | Symbolic link             |
| `env`        | `Get-ChildItem Env:`              | Environment variables     |
| `echo $PATH` | `$env:PATH`                       | Read environment variable |
| `clear`      | `Clear-Host`                      | Clear screen              |
| `tee`        | `Tee-Object`                      | Split pipeline output     |

---

# Important Aliases for Linux Users

PowerShell provides several familiar aliases:

```powershell
ls      # Get-ChildItem
dir     # Get-ChildItem

cd      # Set-Location
pwd     # Get-Location

cp      # Copy-Item
mv      # Move-Item
rm      # Remove-Item

cat     # Get-Content

echo    # Write-Output

clear   # Clear-Host
```

Check what an alias actually means:

```powershell
Get-Alias ls
```

Example:

```text
CommandType Name Definition
----------- ---- ----------
Alias       ls   Get-ChildItem
```

List aliases:

```powershell
Get-Alias
```

---

# Important: Linux Options Do Not Carry Over

Even when PowerShell supports Linux-style aliases:

```powershell
ls
cp
mv
rm
cat
```

the command is still a PowerShell Cmdlet.

For example:

```bash
# Linux
ls -la
```

does NOT mean that PowerShell's `ls` supports GNU `ls` options.

Use:

```powershell
Get-ChildItem -Force
```

Similarly:

```bash
# Linux
rm -rf directory
```

PowerShell equivalent:

```powershell
Remove-Item directory -Recurse -Force
```

not:

```powershell
rm -rf directory
```

---

# PowerShell Pipeline Mental Model

Linux:

```text
Command
   ↓
TEXT
   ↓
grep
   ↓
TEXT
   ↓
awk
```

PowerShell:

```text
Cmdlet
   ↓
OBJECT
   ↓
Where-Object
   ↓
OBJECT
   ↓
Select-Object
```

Example:

```powershell
Get-ChildItem -Recurse -File |
    Where-Object Length -gt 10MB |
    Sort-Object Length -Descending |
    Select-Object Name, Length, FullName
```

Think of it as:

```text
Get objects
    ↓
Filter objects
    ↓
Sort objects
    ↓
Select properties
```

rather than manipulating text.

---

# Commands Worth Memorizing

```powershell
Get-ChildItem
Get-Item
New-Item
Copy-Item
Move-Item
Rename-Item
Remove-Item

Get-Content
Set-Content
Add-Content

Test-Path
Resolve-Path
Join-Path
Split-Path

Where-Object
Select-Object
Sort-Object
Group-Object
Measure-Object

Select-String

Get-Location
Set-Location

Get-Command
Get-Help
```

The general PowerShell naming pattern is:

```text
Verb-Noun
```

Examples:

```powershell
Get-Item
New-Item
Remove-Item

Get-Content
Set-Content

Get-Process
Stop-Process
```

Once you understand the `Verb-Noun` pattern, unfamiliar PowerShell commands become much easier to guess.
