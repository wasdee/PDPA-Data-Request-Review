# Get the current working directory
$directory = Get-Location

# Get all files in the directory that match the pattern *.kb.*
$files = Get-ChildItem $directory -Recurse -Filter *.kb.*

# Loop through each file and run the keybase encrypt command
foreach ($file in $files) {
    $username = "circleoncircles"
    $encrypted_file = Join-Path $file.Directory "$($file.BaseName)$($file.Extension).encrypted"
    $command = "keybase encrypt $username -i ""$($file.FullName)"" -o ""$encrypted_file"""
    Invoke-Expression $command
}
