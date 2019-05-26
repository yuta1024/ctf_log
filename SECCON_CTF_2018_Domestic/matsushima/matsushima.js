const arg = process.argv[2];
const s = arg.indexOf('[');
const e = arg.indexOf(']');

x = eval(arg.substring(s, e+1))
ans = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
x.forEach((e) => {
	ans[Math.floor(e/4)] = ans[Math.floor(e/4)] + 1;
});

ans.forEach((e, i) => {
	if (e == 4) {
		console.log("OK:" + i);
	}
});
