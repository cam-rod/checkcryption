# Checkcryption

Checkcryption is a command line program that helps you share and verify data.

*This is the development branch for the Checkcryption GUI. It is a work in progress, so some parts will have a GUI,
while others will not.*

## How it Works

Checkcryption will encrypt any file using a username and password combination of your choosing. When you want to share the data, send the username and password separately from the actual program and it's encrypted form.

To verify your data, simply sign in, select verify, and point to both files. By encrypting the actual file, the program can compare and ensure that you have obtained the intended version.

## Benefits

* Unlike other checksums, like MD5 and SHA, Checkcryption maintains **the entirety of the file** when encrypted. This program guarantees that every part of the file is the exact same and that you don't just have 2 files that output the same hash.
* Checkcryption offers security thorough an username/password pair. The username ensures that the program is only used by the person with the details. The password creates a unique file, providing an extra bit of verification for small scale sharing.

## Disclaimers

* This project is a **proof-of-concept**. It is not recommended to use this program for any sensitive data, as it is possible to manually undo the encryption if the password is known.
* The password is not recommended for large scale verification by itself, as it must be distributed to verify the file.

## Running the program

For users on Windows, a standalone executable is made available with each stable release. Version 1.0.0 can be found [here](https://github.com/cam-rod/checkcryption/releases/download/1.0.0/checkcryption.exe).

*****

On other devices, the program can be compiled using the latest *develop* version of [PyInstaller](https://github.com/pyinstaller/pyinstaller). Python is required to be installed.

Once PyInstaller and Python are installed, download the zip of Checkcryption from [the latest release](https://github.com/cam-rod/checkcryption/releases/latest) or [the master branch](https://github.com/cam-rod/TI84-colour-physics-bible/archive/master.zip). Extract the zip, and navigate to the top level folder `checkcryption`. Open the command window here, and enter this text to compile the executable:

```shell
pyinstaller --onefile checkcryption.py
```

Navigate to the folder `dist`, and double click `checkcryption.exe` to run the file. Alternatively, run the program directly in Python with the following command:

```shell
python checkcryption.py
```

## Screenshots

***Encryption***  
![Encryption flow](https://i.imgur.com/XL8nLSA.png)

***Verification***  
![Verification flow](https://i.imgur.com/RKTJ2a4.png)

## Contributing

Feel free to fork this project or make pull requests. This program is made available under the MIT license, which can be found [here](LICENSE).
