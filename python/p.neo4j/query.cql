// delete all rels
MATCH ()-[h:HAS]->()
DELETE h;

// delete all nodes
MATCH (a:Area)
DELETE a;

