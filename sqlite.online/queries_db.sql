SELECT 'Tous les produits' as prd , SUM(prix * qte) AS ca FROM ventes;
SELECT produit, SUM(prix * qte) AS ca FROM ventes GROUP BY produit;
SELECT region, SUM(prix * qte) AS ca FROM ventes GROUP BY region;