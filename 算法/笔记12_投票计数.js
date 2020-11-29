// 法一：投票的同时计数，一开始就使用散列表收集票数
//O(1)

var votes = {};

function add_vote(candidate) {
	if(votes[candidate]) {
		votes[candidate]==;
	} else {
		votes[candidate] = 1;
	}
}

function count_votes() {
	return votes;

// 法二：O(N)，票都在数组votes里
function count_votes(votes) {
	var tally = {};
	for(var i = 0; i < votes.length; i++) {
		if(tally[votes[i]]) {
			tally[votes[i]]++;
		} else {
			tally[votes[i]] = 1;
		}
	}
	return tally;
}