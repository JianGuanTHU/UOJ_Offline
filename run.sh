path=/Users/jian/Jian/Lab/2020oop/offline_env/UOJ_Offline
filename="./"
id=`python2 ./find_problem_id.py`
rm -r ./work
rm -r ./result
rm ./judger
mkdir ./result
mkdir ./work
cp -r ./data/$id/1/submit/* ./work
cp -r ./data/$id/1/require/* ./work
cp -r ./data/$id/1/judger ./
python2 ./judger $path $path/work $path/result/ $path/data/$id/1
cat ./result/result.txt
rm ./judger