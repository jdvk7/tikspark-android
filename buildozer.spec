
[app]

title = TikSpark
package.name = tikspark
package.domain = org.jdvk7

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,txt,json

version = 1.0.0

requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 35
android.minapi = 23
android.archs = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 1
