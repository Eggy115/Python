import win32com.shell.shell as shell
shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+"start powershell") # tries powershell using cmd
shell.ShellExecuteEx(lpVerb='runas', lpFile='powershell.exe', lpParameters='/c '+"start powershell") # tries powershell using powershell
shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+"start cmd") # tries cmd using cmd
shell.ShellExecuteEx(lpVerb='runas', lpFile='powershell.exe', lpParameters='/c '+"start cmd") # tries cmd using powershell
