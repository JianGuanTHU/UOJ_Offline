import sys
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

input, output, answer = sys.argv[1:]

f_in = open(input)
f_out = open(output)
f_answer = open(answer)

f_in_lines = f_in.readlines()

ref_ans, n, m = int(f_in_lines[0].strip()), int(f_in_lines[1].strip()), int(f_in_lines[2].strip())
k = int(f_in_lines[m+3].strip())

f_answer_lines = f_answer.readlines()

f_out_lines = f_out.readlines()
score = 0

for i in range(k):
	if f_out_lines[i].strip() != f_answer_lines[i].strip():
		eprint("Wrong answer at the line %d." % (i+1))
		sys.exit(0)

cnt = list(map(int, f_out_lines[k].strip().split()))

if cnt[0] + cnt[1] + cnt[2] != cnt[5]:
	eprint("Memory leak detected. Construction times: %d. Destruction times: %d" % 
		(cnt[0] + cnt[1] + cnt[2], cnt[5]))
	sys.exit(0)
		
tmp = (cnt[0] + cnt[1] + cnt[3]) * 10 + cnt[2] + cnt[4]
if tmp <= ref_ans:
	assert f_out_lines[k+1].strip() == "YES"
	eprint("ok")
else:
	assert f_out_lines[k+1].strip() == "NO"
	eprint("points 0.7\nYour count times: %s > %d" % (f_out_lines[k].strip(), ref_ans))
