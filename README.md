# <img src="Thumbnail/rng-ish.png" alt="rng-ish Icon" width="32"> rng-ish
A python program that prints a random number from 1 - 100

### Compiling rng-ish

- Install pyinstaller and rich using pip
 ```
 pip install pyinstaller rich
 ``` 

- Using pipx
```
pipx install pyinstaller
pipx inject pyinstaller rich
```

- Clone this Repository
```
git clone https://github.com/ultraindv/rng-ish
```

- Cd into the directory
```
cd rng-ish
```

- Compile rng-ish using pyinstaller
```
pyinstaller --onefile --copy-metadata rich rng-ish.py
```

### (Optional) Compile Into an AppImage:
To make and compile into an AppImage:
- Download linuxdeploy as an AppImage and make sure its executable
```
chmod +x linuxdeploy-<arch>.AppImage
```

- Compile rng-ish using pyinstaller(Refer to Compiling rng-ish) and move the executable in to `rng-ish.AppDir/usr/bin`
```
mv dist/rng-ish rng-ish.AppDir/usr/bin/
```

-  use linuxdeploy to compile into an AppImage
```
./linuxdeploy-<arch>.AppImage --appdir rng-ish.AppDir --output appimage
