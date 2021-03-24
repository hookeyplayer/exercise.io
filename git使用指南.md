//创建仓库（含readme打勾）
git clone 仓库地址
//完成上述，本地就会有一个仓库名的文件夹了
cd 仓库名


//初始化仓库，名叫git-tutorial
mkdir git-tutorial
cd git-tutorial
git init
//完成上述，生成一个.git的目录，存储着管理当前目录内容所需的仓库数据，是一棵工作树

git status
touch README.md
//在目录中就会出现这个markdown文件

//暂存
git add README.

//查看本次提交和上次提交的差别
git diff HEAD

//提交
git commit -m "add this markdown file"


//查看提交
git log

git log --pretty=short

git log命令后加上目录名，便会只显示该目录下的日志。 如果加的是文件名，就会只显示与该文件相关的日志。

//前后变动的查看
git log -p

//工作树和暂存区的前后变动
git diff
git diff HEAD

//仓库更新
git push

//显示分支名
git branch

//创建叫做feature-A的分支，并将当前分支切换为feature-A
git checkout -b feature-A (精炼的方法)

git branch feature-A
git checkout feature-A(两句同样的效果)






