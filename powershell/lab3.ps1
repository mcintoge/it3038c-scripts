function getIP{
    (get-netipaddress).ipv4address | Select-String "192*"
}
$IP = getIP

function getUSER{
    (Get-LocalUser) | Select-String "Admin*"
}
$USER = getUSER

function getVER{
(Get-Host).Version

}
$VER = getVER

function getNAM{
$env:COMPUTERNAME
}  
$NAM = getNAM

function getdate{
Get-Date -Format "dddd MM/dd/yyyy"

}
$DATE = getDATE


$From = "ginnaeayenew@gmail.com"

$To = "leonardf@ucmail.uc.edu"

$Subject = " IT3038C Windows SysInfo"

$BODY = "This machine's IP is $IP. User is $USER. Hostname is $NAM. Powershell veriosn $VER. Today's date is $DATE."
 

$Password = "ywpkaxuvyssodyqb" | ConvertTo-SecureString -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $From, $Password
Send-MailMessage -From $From -To $To -Subject $Subject -Body $Body -SmtpServer "smtp.gmail.com" -port 587 -UseSsl -Credential $Credential