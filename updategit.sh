UPDATE=$(date +%Y%m%d)

git init
git add *
git commit -m "commit${UPDATE}"
git remote add origin https://github.com/mbenedicto99/py.git
git push -u origin master
