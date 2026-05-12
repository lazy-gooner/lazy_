INSERT or IGNORE INTO Speles_normunda VALUES("S_003","project lobotomy","PC","simulator","18","2018",25.99);
INSERT or IGNORE INTO Speles_normunda VALUES("S_004","library of ruina","PC","strategy","18","2020",29.99);
SELECT  Speles_id, Nosaukums, Platforma, Zanrs, Vecuma_ierobezojums, Izdosanas_gads, Cena FROM Speles_normunda;
SELECT max(Cena) FROM Speles_normunda;
SELECT sum(Cena) FROM Speles_normunda;
SELECT avg(Izdosanas_gads) FROM Speles_normunda;
SELECT min(Izdosanas_gads) FROM Speles_normunda;
SELECT Nosaukums, Platforma, Cena FROM Speles_normunda;

