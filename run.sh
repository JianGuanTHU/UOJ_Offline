path=/Users/jian/Jian/Lab/2021oop/UOJ_Offline
filename="./"
rm -r ./work
rm -r ./result
rm ./judger
mkdir ./result
mkdir ./work
id=`python2 ./find_problem_id.py`
cp -r ./data/$id/1/submit/* ./work
cp ./data/$id/1/require/* ./work
cp -r ./data/$id/1/judger ./
python_version=`python2 ./find_python_version.py $id`
$python_version ./judger $path $path/work $path/result/ $path/data/$id/1
cat ./result/result.txt
rm ./judger