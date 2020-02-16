import pandas as pd

path = r' insira pasta com dados aqui'

desp_col = path + "DESPESA_COLETIVA.csv"
despesas = pd.read_csv(desp_col)

inss_cod = [
 1900101, 1900102, 1900201, 1900202, 1900301, 1900302, 1900401, 1900402,
 1900501, 1900502, 1900601, 1900602, 1900701, 1900801, 1900901, 1901001, 
 1901101, 1901201, 1901202, 1901203, 1901204, 1901301, 1901302, 1901401, 
 1901402, 1901501, 1901601, 1901701, 1999901, 4800501, 4800502, 5300101, 
 5300201, 5300301, 5300401, 5300501, 5300601
 ]

ir_cod = [
 4803101, 4803102, 5300101, 5300201, 5300301, 5300401, 5300501, 5300601
 ]
 
ipva_cod = [
 5000101, 5000102, 5000103, 5000401, 5000402, 5000501, 5000502, 5000601, 
 5000602, 5000701, 5000801, 5000802, 5000803, 5000804, 5000805, 5000806,
 5000807, 5000808, 5000809, 5000810, 5000811, 5000812, 5000813, 5000814,
 5000815, 5000816, 5001601, 5001701, 5001401
 ]

iptu_cod = [ 
 1000601, 1000602, 1001101, 4700601, 1000701, 1000702, 1000703, 1001201,
 4700701, 1001401, 1001301, 4702601, 1001501, 1001601, 1203501
 ]

outros_cod = [ 4800401, 4803701, 4801001, 4801002, 4801003, 4801101, 4801102 ]

aposetnadorias = [5400401, 5400501, 5500301, 5500401, 5505001, 5400601, 5400701, 5500501, 5500601, 5504701]

BPC = [5400201, 5402401]

auxilios = [5505601, 5400901, 5402701, 5403001, 5503601, 5503602, 5503603, 5505501, 5504501, 5402401,]

seguro_desemprego = [5501701,5501702]

transferências =[ 5400103,5400104,5400105,5400106,5400107,5400108,5400301,5400302,
5400303,5400304,5400305,5400306,5400307,5400308,5400309,5400310,5400311,5400312,
5400313,5400314,5400315,5400316,5400317,5402301,5501801,5505201,5506501,5501901]

bolsa_familia =  [5400101,5400102,5506601]

outras_aposentadorias_pensões = [5403101,13145506401,5400801,5402901,5503301,13145500701,5401101,13145506301,5505701,5402901]

df_final = despesas.copy()
df_final.index = (df_final.UF.map(str) + df_final['COD_UPA'].map(str) + df_final['NUM_DOM'].map(str)).map(int)

def aggregate(df, cod):
    df.UF = (df.UF.map(str) + df['COD_UPA'].map(str) + df['NUM_DOM'].map(str)).map(int)
    df_local = df[df.V9001.isin(cod)]
    df_local_values = pd.DataFrame(df_local.V8000.values, index = df_local.UF)
    return  df_local_values.groupby(df_local_values.index).agg({0 : sum })

df_final['FAMILIA'] = df_final.index
df_final['INSS'] = aggregate(despesas, inss_cod)
df_final['IR'] = aggregate(despesas, ir_cod)
df_final['IPVA'] = aggregate(despesas, ipva_cod)
df_final['IPTU'] = aggregate(despesas, iptu_cod)
df_final['OUTROS_IMOPSTOS'] = aggregate(despesas, outros_cod)
# %%
df_final = df_final.loc[:,['FAMILIA','INSS','IR','IPVA','IPTU','OUTROS_IMPOSTOS','PESO','RENDA_TOTAL']]
df_final = df_final.drop_duplicates(subset='FAMILIA',keep='first').reset_index(drop=True)