// https://www.urionlinejudge.com.br/judge/pt/problems/view/1152
const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n');
let [V, E] = lines.shift().split(' ').map(x => parseInt(x));
let src, dest, weight;

const findSet = (SUBSETS, index) => {
  if (SUBSETS[index] != index) {
    SUBSETS[index] = findSet(SUBSETS, SUBSETS[index]); // with path compression
  }

  return SUBSETS[index];
}

while (V != 0 && E != 0) {
  let EDGES = []; // src - dest - weight
  let SUBSETS = []; // [vertix] = father
  let OPTIMAL = [];

  count_E = E;
  while (count_E--) {
    // READING EDGE
    [src, dest, weight] = lines.shift().split(' ').map(x => parseInt(x));
    const actual = {
      src,
      dest,
      weight,
    };
    EDGES.push(actual);

    // ORDERING WITH INSERTION TO BE FASTER
    let offset = EDGES.length - 1;
    while (offset > 0 && EDGES[offset - 1].weight > actual.weight) {
      EDGES[offset] = EDGES[offset - 1];
      offset--;
    }
    offset = offset < 0 ? 0 : offset;
    EDGES[offset] = actual;
  }

  // MOUNTING UNION FIND SUBSETS
  for (let i = 0; i < V; ++i) {
    SUBSETS.push(i);
  }

  // console.log(EDGES, EDGES.length);
  // console.log(SUBSETS, SUBSETS.length);

  // GREEDY
  EDGES.forEach(edge => {
    if (findSet(SUBSETS, edge.src) != findSet(SUBSETS, edge.dest)) {
      SUBSETS[findSet(SUBSETS, edge.dest)] = findSet(SUBSETS, edge.src);
      OPTIMAL.push(edge);
    }
  });

  // console.log(OPTIMAL, OPTIMAL.length);
  total_weight = EDGES.reduce((prev, curr) => prev + curr.weight, 0);
  min_weight = OPTIMAL.reduce((prev, curr) => prev + curr.weight, 0);
  console.log(total_weight, min_weight);
  // console.log(total_weight - min_weight);

  [V, E] = lines.shift().split(' ').map(x => parseInt(x));
}

