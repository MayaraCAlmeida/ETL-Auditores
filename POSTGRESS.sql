-- AUDITORES PF

DROP TABLE IF EXISTS public.cad_auditor_pf;

CREATE TABLE public.cad_auditor_pf (
    cd_cvm     INTEGER,
    auditor    TEXT,
    sit        TEXT,
    dt_ini_sit DATE
);

INSERT INTO public.cad_auditor_pf (cd_cvm, auditor, sit, dt_ini_sit)
VALUES
    (9059,  'AGUIAR ARAUJO DE OLIVEIRA', 'ATIVO', '2001-07-13'),
    (10600, 'ALBERTO FRANCISCO COSTA',   'ATIVO', '2006-09-01'),
    (11363, 'ALEX RIBEIRO TELO',         'ATIVO', '2009-11-27');

-- todos os registros
SELECT * FROM public.cad_auditor_pf;

-- utilizando AS pra melhorar a nomeação de colunas
SELECT
    cd_cvm     AS id_auditor,
    auditor    AS nome,
    sit        AS situacao,
    dt_ini_sit AS data_inicio
FROM public.cad_auditor_pf;

-- apenas ativos
SELECT * FROM public.cad_auditor_pf
WHERE sit = 'ATIVO'
ORDER BY dt_ini_sit DESC;


-- AUDITORES PJ

DROP TABLE IF EXISTS public.cad_auditor_pj;

CREATE TABLE public.cad_auditor_pj (
    cd_cvm     INTEGER,
    cnpj       TEXT,
    denom_social TEXT,
    sit        TEXT,
    dt_ini_sit DATE,
    tp_ender   TEXT,
    logradouro TEXT,
    compl      TEXT,
    bairro     TEXT,
    mun        TEXT,
    uf         CHAR(2),
    cep        TEXT
);

INSERT INTO public.cad_auditor_pj (cd_cvm, cnpj, denom_social, sit, dt_ini_sit, tp_ender, logradouro, compl, bairro, mun, uf, cep)
VALUES
    (9164, '36.348.092/0001-42', 'A.C.A. - AUDITORIA E CONSULTORIA',                   'ATIVO', '2001-10-08', 'SEDE', 'AV. NOSSA SENHORA DOS NAVEGANTES, ED. PALACIO DO CAFE 675', 'SL 102/103',  'ENSEADA DO SUÁ', 'VITÓRIA',       'ES', '29050912'),
    (9482, '05.209.294/0001-80', 'ACCOUNT - AUDITORES INDEPENDENTES S/S',               'ATIVO', '2002-09-19', 'SEDE', 'RUA SIRIRI, 496',                                           '1º AND SL 03', 'CENTRO',         'ARACAJU',       'SE', '49010450'),
    (5517, '20.763.801/0001-16', 'ACE AUDITORIA ASSESSORIA E CONSULTORIA EMPRESARIAL',  'ATIVO', '1992-05-25', 'SEDE', 'AV BARÃO HOMEM DE MELO, 4500',                              'SALA 1011',   'ESTORIL',        'BELO HORIZONTE', 'MG', '30494270');

-- todos os registros
SELECT * FROM public.cad_auditor_pj;

-- utilizando AS pra melhorar a nomeação de colunas
SELECT
    cd_cvm       AS id_auditor,
    cnpj         AS cnpj,
    denom_social AS razao_social,
    sit          AS situacao,
    dt_ini_sit   AS data_inicio,
    mun          AS municipio,
    uf
FROM public.cad_auditor_pj;

-- filtrar por estado
SELECT * FROM public.cad_auditor_pj
WHERE uf = 'MG'
ORDER BY denom_social;

