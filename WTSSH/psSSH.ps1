
function ssh-copy-id([string]$userAtMachine){   
    $publicKey = "$ENV:USERPROFILE" + "/.ssh/id_rsa.pub"
    if (!(Test-Path "$publicKey")){
        Write-Error "ERROR: failed to open ID file '$publicKey': No such file"            
    }
    else {
        & cat "$publicKey" | ssh $userAtMachine "umask 077; test -d .ssh || mkdir .ssh ; cat >> .ssh/authorized_keys || exit 1"   
        # & cat "$publicKey" | ssh $userAtMachine "umask 077; test -d .ssh || mkdir .ssh ; cat >> .ssh/authorized_keys || exit 1"   
        "success : write publickey into " +$userAtMachine
    }
}



#读取配置文件
[string]$configFile= "C:\\mySoftware\\psSSH\\psSSHConfig.json"
$CONF = (Get-Content $configFile) | ConvertFrom-Json
$serverList = $CONF.serverList
If($serverList -eq $null) {
    "error in reading config file"
    break
}

$index = 0
foreach($oneServer in $serverList){
    $serverHost = $oneServer.host
    $serverUser = $oneServer.user
    $serverPassword = $oneServer.password
    $serverauth = $oneServer.auth
    $serverAlias = $oneServer.alias

    "server index {0}
        name: {1}
        host: {2}
        user: {3}
        auth: {4}
    " -f $index,$serverAlias,$serverHost,$serverUser,$serverauth
    $index = $index+1
}

"please input the index to login:"
while($true)
{
    [int]$nowIndex = Read-Host
    if (($nowIndex -ge 0) -and ($nowIndex -lt $serverList.count)) {
        $nowServer = $serverList[$nowIndex]
        $serverHost = $nowServer.host
        $serverUser = $nowServer.user
        $serverPassword = $nowServer.password
        $serverauth = $nowServer.auth
        $serverAlias = $nowServer.alias

        $url=[string]($serverUser+"@"+$serverHost)
        $url
        if ($serverauth -eq 0) {
            ssh-copy-id($url)
            $serverList[$nowIndex].auth=1
            $CONF | ConvertTo-Json | Set-Content -Path $configFile
        }
        ssh $url
        break
    }else {
        "index is not allowed,please input again:"
    }
}

Read-Host