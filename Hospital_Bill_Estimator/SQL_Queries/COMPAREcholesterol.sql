SELECT 'Anmed' AS [Source], [Description], [Cash_Price]
FROM [dbo].[Anmedcannonstandardcharges - Output]
WHERE [Description] IN ('HC CHOLESTEROL SERUM/WHOLE BLOOD TOTAL','HC COMPREHENSIVE METABOLIC PANEL', 'HC LIPID PANEL', 'HC BLOOD COUNT COMPLETE AUTOMATED')

UNION 

SELECT 'Prisma' AS [Source], [Description],[Discounted_Cash_Price] 
FROM [dbo].[PrismaHealth_TuomeyHospital_standardcharges - Output]
WHERE [Description] IN ('HC CHOLESTEROL SERUM OR WHOLE BLOOD TOTAL','COMPREHEN METABOLIC PANEL','HC LIPID PANEL','HC BLOOD COUNT CBC AUTOMATED W/AUTOMATED DIFF')
