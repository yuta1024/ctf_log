#/bin/sh

for m in {20..59}; do
	for s in {0..59}; do
		t="12/23 04:${m}:${s} 2018"
		echo $t
		sudo date -s "${t}" >/dev/null && ./generate_random_hands | xargs node matsushima.js
	done
done
