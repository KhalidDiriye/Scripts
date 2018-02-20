//Credit to creator
If WScript.Arguments.count <> 2 Then WScript.Quit

Const wbemFlagReturnImmediately = &h10
Const wbemFlagForwardOnly = &h20
Dim objWMIService, UserAccount, myComputer, UserSID, CurrentUser
Dim oShell, RegKey, RegVal

RegVal = WScript.Arguments.Item(1)

Set oShell = CreateObject("Wscript.Shell")

If LoadHive() = True Then
    RegKey = "HKEY_USERS\defUser\" & WScript.Arguments.Item(0)
    DoRegChange RegKey, RegVal
    UnloadHive
End If



Sub DoRegChange(RegKey, RegVal)
      WScript.Sleep 1000
      oShell.RegWrite RegKey, RegVal
End Sub

Function LoadHive()
      Set oFSO = CreateObject("Scripting.FileSystemObject")
      If oFSO.FileExists("C:\Documents And Settings\Default User\NTUser.Dat") Then
            oShell.Exec "Reg load " & "HKU\defUser " & """C:\Documents And Settings\Default User\NTUser.Dat"""
            LoadHive = True
      Else
            LoadHive = False
      End If
End Function

Sub UnloadHive()
      oShell.Exec "Reg unload " & "HKU\defUser"
End Sub