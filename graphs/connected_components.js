// https://www.urionlinejudge.com.br/judge/pt/problems/view/1082
const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n');
let T = parseInt(lines.shift());

let V, E;
let src, dest;
let AdjSet;
let answers;
let path;
let visited_vertex;
let count = 1;

const dfs = (vertex, path) => {
  if (visited_vertex[vertex] === 1) {
    return;
  }

  visited_vertex[vertex] = 1;
  path.push(String.fromCharCode('a'.charCodeAt() + vertex));

  Array.from(AdjSet[vertex]).forEach(element => {
    if (visited_vertex[element] === 0) {
      dfs(element, path);
    }
  });
}

while (T--) {
  [V, E] = lines.shift().split(' ').map(x => parseInt(x));
  AdjSet = [];
  visited_vertex = []; // 0 non visited - 1 visited
  answers = [];

  for (let index = 0; index < V; index++) {
    AdjSet[index] = new Set();
    visited_vertex[index] = 0;
  }

  for (let index = 0; index < E; index++) {
    [src, dest] = lines.shift().split(' ').map(x => x.charCodeAt() - 'a'.charCodeAt());
    AdjSet[src].add(dest);
    AdjSet[dest].add(src);
  }

  for (let index = 0; index < V; index++) {
    path = [];
    dfs(index, path);
    if (path.length > 0) {
      answers.push(path);
    }
  }

  console.log(`Case #${count}:`)
  answers.forEach(path => {
    console.log(path.sort().reduce((prev,curr) => `${prev}${curr},`,''));
  });
  console.log(`${answers.length} connected components`)
  // console.log(answers);
  // console.log(AdjSet);
  console.log();
  count ++;
}

