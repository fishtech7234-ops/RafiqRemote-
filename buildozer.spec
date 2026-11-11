[app]
title = Rafiq Remote
package.name = rafiqremote
package.domain = org.fishtech
source.dir = .
source.include_exts = py,png,jpg,kv
version = 1.0

requirements = python3,kivy
orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 23
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
