[[package]]
category = "main"
description = "NumPy is the fundamental package for array computing with Python."
name = "numpy"
optional = false
python-versions = ">=3.5"
version = "1.18.5"

[[package]]
category = "main"
description = "Powerful data structures for data analysis, time series, and statistics"
name = "pandas"
optional = false
python-versions = ">=3.6.1"
version = "1.0.5"

[package.dependencies]
numpy = ">=1.13.3"
python-dateutil = ">=2.6.1"
pytz = ">=2017.2"

[package.extras]
test = ["pytest (>=4.0.2)", "pytest-xdist", "hypothesis (>=3.58)"]

[[package]]
category = "main"
description = "Extensions to the standard Python datetime module"
name = "python-dateutil"
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,>=2.7"
version = "2.8.1"

[package.dependencies]
six = ">=1.5"

[[package]]
category = "main"
description = "World timezone definitions, modern and historical"
name = "pytz"
optional = false
python-versions = "*"
version = "2020.1"

[[package]]
category = "main"
description = "Python 2 and 3 compatibility utilities"
name = "six"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*"
version = "1.15.0"

[metadata]
content-hash = "88898649b2c2795ec8c90186c7af96f35e2020bea9f323ce8b174a0fdccfb00b"
python-versions = "^3.8"

[metadata.files]
numpy = [
    {file = "numpy-1.18.5-cp35-cp35m-macosx_10_9_intel.whl", hash = "sha256:e91d31b34fc7c2c8f756b4e902f901f856ae53a93399368d9a0dc7be17ed2ca0"},
    {file = "numpy-1.18.5-cp35-cp35m-manylinux1_i686.whl", hash = "sha256:7d42ab8cedd175b5ebcb39b5208b25ba104842489ed59fbb29356f671ac93583"},
    {file = "numpy-1.18.5-cp35-cp35m-manylinux1_x86_64.whl", hash = "sha256:a78e438db8ec26d5d9d0e584b27ef25c7afa5a182d1bf4d05e313d2d6d515271"},
    {file = "numpy-1.18.5-cp35-cp35m-win32.whl", hash = "sha256:a87f59508c2b7ceb8631c20630118cc546f1f815e034193dc72390db038a5cb3"},
    {file = "numpy-1.18.5-cp35-cp35m-win_amd64.whl", hash = "sha256:965df25449305092b23d5145b9bdaeb0149b6e41a77a7d728b1644b3c99277c1"},
    {file = "numpy-1.18.5-cp36-cp36m-macosx_10_9_x86_64.whl", hash = "sha256:ac792b385d81151bae2a5a8adb2b88261ceb4976dbfaaad9ce3a200e036753dc"},
    {file = "numpy-1.18.5-cp36-cp36m-manylinux1_i686.whl", hash = "sha256:ef627986941b5edd1ed74ba89ca43196ed197f1a206a3f18cc9faf2fb84fd675"},
    {file = "numpy-1.18.5-cp36-cp36m-manylinux1_x86_64.whl", hash = "sha256:f718a7949d1c4f622ff548c572e0c03440b49b9531ff00e4ed5738b459f011e8"},
    {file = "numpy-1.18.5-cp36-cp36m-win32.whl", hash = "sha256:4064f53d4cce69e9ac613256dc2162e56f20a4e2d2086b1956dd2fcf77b7fac5"},
    {file = "numpy-1.18.5-cp36-cp36m-win_amd64.whl", hash = "sha256:b03b2c0badeb606d1232e5f78852c102c0a7989d3a534b3129e7856a52f3d161"},
    {file = "numpy-1.18.5-cp37-cp37m-macosx_10_9_x86_64.whl", hash = "sha256:a7acefddf994af1aeba05bbbafe4ba983a187079f125146dc5859e6d817df824"},
    {file = "numpy-1.18.5-cp37-cp37m-manylinux1_i686.whl", hash = "sha256:cd49930af1d1e49a812d987c2620ee63965b619257bd76eaaa95870ca08837cf"},
    {file = "numpy-1.18.5-cp37-cp37m-manylinux1_x86_64.whl", hash = "sha256:b39321f1a74d1f9183bf1638a745b4fd6fe80efbb1f6b32b932a588b4bc7695f"},
    {file = "numpy-1.18.5-cp37-cp37m-win32.whl", hash = "sha256:cae14a01a159b1ed91a324722d746523ec757357260c6804d11d6147a9e53e3f"},
    {file = "numpy-1.18.5-cp37-cp37m-win_amd64.whl", hash = "sha256:0172304e7d8d40e9e49553901903dc5f5a49a703363ed756796f5808a06fc233"},
    {file = "numpy-1.18.5-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:e15b382603c58f24265c9c931c9a45eebf44fe2e6b4eaedbb0d025ab3255228b"},
    {file = "numpy-1.18.5-cp38-cp38-manylinux1_i686.whl", hash = "sha256:3676abe3d621fc467c4c1469ee11e395c82b2d6b5463a9454e37fe9da07cd0d7"},
    {file = "numpy-1.18.5-cp38-cp38-manylinux1_x86_64.whl", hash = "sha256:4674f7d27a6c1c52a4d1aa5f0881f1eff840d2206989bae6acb1c7668c02ebfb"},
    {file = "numpy-1.18.5-cp38-cp38-win32.whl", hash = "sha256:9c9d6531bc1886454f44aa8f809268bc481295cf9740827254f53c30104f074a"},
    {file = "numpy-1.18.5-cp38-cp38-win_amd64.whl", hash = "sha256:3dd6823d3e04b5f223e3e265b4a1eae15f104f4366edd409e5a5e413a98f911f"},
    {file = "numpy-1.18.5.zip", hash = "sha256:34e96e9dae65c4839bd80012023aadd6ee2ccb73ce7fdf3074c62f301e63120b"},
]
pandas = [
    {file = "pandas-1.0.5-cp36-cp36m-macosx_10_9_x86_64.whl", hash = "sha256:faa42a78d1350b02a7d2f0dbe3c80791cf785663d6997891549d0f86dc49125e"},
    {file = "pandas-1.0.5-cp36-cp36m-manylinux1_i686.whl", hash = "sha256:9c31d52f1a7dd2bb4681d9f62646c7aa554f19e8e9addc17e8b1b20011d7522d"},
    {file = "pandas-1.0.5-cp36-cp36m-manylinux1_x86_64.whl", hash = "sha256:8778a5cc5a8437a561e3276b85367412e10ae9fff07db1eed986e427d9a674f8"},
    {file = "pandas-1.0.5-cp36-cp36m-win32.whl", hash = "sha256:9871ef5ee17f388f1cb35f76dc6106d40cb8165c562d573470672f4cdefa59ef"},
    {file = "pandas-1.0.5-cp36-cp36m-win_amd64.whl", hash = "sha256:35b670b0abcfed7cad76f2834041dcf7ae47fd9b22b63622d67cdc933d79f453"},
    {file = "pandas-1.0.5-cp37-cp37m-macosx_10_9_x86_64.whl", hash = "sha256:c9410ce8a3dee77653bc0684cfa1535a7f9c291663bd7ad79e39f5ab58f67ab3"},
    {file = "pandas-1.0.5-cp37-cp37m-manylinux1_i686.whl", hash = "sha256:02f1e8f71cd994ed7fcb9a35b6ddddeb4314822a0e09a9c5b2d278f8cb5d4096"},
    {file = "pandas-1.0.5-cp37-cp37m-manylinux1_x86_64.whl", hash = "sha256:b3c4f93fcb6e97d993bf87cdd917883b7dab7d20c627699f360a8fb49e9e0b91"},
    {file = "pandas-1.0.5-cp37-cp37m-win32.whl", hash = "sha256:5759edf0b686b6f25a5d4a447ea588983a33afc8a0081a0954184a4a87fd0dd7"},
    {file = "pandas-1.0.5-cp37-cp37m-win_amd64.whl", hash = "sha256:ab8173a8efe5418bbe50e43f321994ac6673afc5c7c4839014cf6401bbdd0705"},
    {file = "pandas-1.0.5-cp38-cp38-macosx_10_9_x86_64.whl", hash = "sha256:13f75fb18486759da3ff40f5345d9dd20e7d78f2a39c5884d013456cec9876f0"},
    {file = "pandas-1.0.5-cp38-cp38-manylinux1_i686.whl", hash = "sha256:5a7cf6044467c1356b2b49ef69e50bf4d231e773c3ca0558807cdba56b76820b"},
    {file = "pandas-1.0.5-cp38-cp38-manylinux1_x86_64.whl", hash = "sha256:ae961f1f0e270f1e4e2273f6a539b2ea33248e0e3a11ffb479d757918a5e03a9"},
    {file = "pandas-1.0.5-cp38-cp38-win32.whl", hash = "sha256:f69e0f7b7c09f1f612b1f8f59e2df72faa8a6b41c5a436dde5b615aaf948f107"},
    {file = "pandas-1.0.5-cp38-cp38-win_amd64.whl", hash = "sha256:4c73f373b0800eb3062ffd13d4a7a2a6d522792fa6eb204d67a4fad0a40f03dc"},
    {file = "pandas-1.0.5.tar.gz", hash = "sha256:69c5d920a0b2a9838e677f78f4dde506b95ea8e4d30da25859db6469ded84fa8"},
]
python-dateutil = [
    {file = "python-dateutil-2.8.1.tar.gz", hash = "sha256:73ebfe9dbf22e832286dafa60473e4cd239f8592f699aa5adaf10050e6e1823c"},
    {file = "python_dateutil-2.8.1-py2.py3-none-any.whl", hash = "sha256:75bb3f31ea686f1197762692a9ee6a7550b59fc6ca3a1f4b5d7e32fb98e2da2a"},
]
pytz = [
    {file = "pytz-2020.1-py2.py3-none-any.whl", hash = "sha256:a494d53b6d39c3c6e44c3bec237336e14305e4f29bbf800b599253057fbb79ed"},
    {file = "pytz-2020.1.tar.gz", hash = "sha256:c35965d010ce31b23eeb663ed3cc8c906275d6be1a34393a1d73a41febf4a048"},
]
six = [
    {file = "six-1.15.0-py2.py3-none-any.whl", hash = "sha256:8b74bedcbbbaca38ff6d7491d76f2b06b3592611af620f8426e82dddb04a5ced"},
    {file = "six-1.15.0.tar.gz", hash = "sha256:30639c035cdb23534cd4aa2dd52c3bf48f06e5f4a941509c8bafd8ce11080259"},
]
