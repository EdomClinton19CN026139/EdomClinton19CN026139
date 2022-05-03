loc_D = float(input('Enter mean of dolomite:'))
loc_S = float(input('Enter mean of shale:'))
scale_D = float(input('Enter Standard Deviation of dolomite:'))
scale_S = float(input('Enter Standard Deviation of shale:'))
count_D = float(input('Enter count of dolomite:'))
count_S = float(input('Enter count of shale:'))
import scipy.stats               
No_cores = count_D + count_S
p_D = count_D/No_cores
p_S = count_S/No_cores
P_D_gamma_greater_than_60 = 1-scipy.stats.norm(loc_D,scale_D).cdf(0.5)
P_S_gamma_greater_than_60 = 1- scipy.stats.norm(loc_S,scale_S).cdf(0.5)
P_Dm_gamma_greater_than_60 = (p_D*P_D_gamma_greater_than_60)/(p_D*P_D_gamma_greater_than_60)+( p_S*P_S_gamma_greater_than_60)
if P_Dm_gamma_greater_than_60>=0.5:
    print('DOLOMITE')
else:
    print('SHALE')
  



