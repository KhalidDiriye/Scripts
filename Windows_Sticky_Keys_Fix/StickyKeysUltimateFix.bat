@ECHO OFF
ECHO Disabling Sticky Keys for the Default User
alterDefaultUSer.vbs "Control Panel\Accessibility\Keyboard Response\\Flags" "122"
alterDefaultUSer.vbs "Control Panel\Accessibility\StickyKeys\\Flags" "506"
alterDefaultUSer.vbs "Control Panel\Accessibility\ToggleKeys\\Flags" "58"
regedit /s stickykeys.reg