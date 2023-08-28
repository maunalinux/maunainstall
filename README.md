# Maunainstall

Software Manager for Mauna Linux.

![image](https://user-images.githubusercontent.com/19881231/122644976-86767180-d120-11eb-9cf4-eed2813f749b.png)

## Build
Get source code
```
git clone https://github.com/maunalinux/maunainstall
cd maunainstall
```
Build
```
dpkg-buildpackage --no-sign
```
Install
```
cd ..
sudo install ./maunainstall*.deb
```

