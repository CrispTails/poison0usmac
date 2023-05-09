import OS

os.system("sudo chflags norestricted /")
os.system("sudo chmod 777 /")
os.system("sudo touch /.mount_rw")
os.system("sudo chmod 777 /.mount_rw")
os.system("sudo chmod +s /usr/libexec/authopen")
os.system("sudo defaults write com.apple.finder AppleShowAllFiles YES")
os.system("sudo defaults write com.apple.finder AppleShowAllFiles -bool true")
os.system("killall Finder")
os.system("sudo spctl --master-disable")
os.system("sudo nvram boot-args='recovery-mode=unused'")
print("If you're seeing this then you must be debugging.")
