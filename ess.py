#10/24/18 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

ess=pd.read_csv("ESS1-7e01.csv")
ess.shape

#nordic countries
nordic=ess[(ess['cntry']=="DK")| (ess['cntry']=="SE") | (ess['cntry']=="FI") | (ess['cntry']=="IS") |(ess['cntry']=="NO")]

#I. MEDIA 
#create group media average index
n_media=nordic[["tvtot","rdtot","nwsptot","netuse","pplfair","ppltrst","pplhlp"]]
n_media['rdtot'].min() 
n_media=n_media.dropna()
n_media.info()

n_media['tvtot']=n_media["tvtot"].astype('category')
n_media_count=n_media.groupby("tvtot").count()

#media counts
tv=n_media['tvtot'].value_counts()
radio=n_media['rdtot'].value_counts()
news=n_media['nwsptot'].value_counts()
net=n_media['netuse'].value_counts()
ppl_fair=n_media['pplfair'].value_counts()
ppl_trust=n_media['ppltrst'].value_counts() 

media_counts=pd.concat([tv,radio,news,net,ppl_fair,ppl_trust], axis=1)
media_pcts=media_counts.iloc[:, 0:].apply(lambda x: (x / x.sum()*100))
media_pcts.fillna(0)

#correlation matrix
media_pcts.corr()
fig=plt.figure()
plt.matshow(media_pcts.corr())
plt.savefig('media_corr.png')

#II. POLITICAL TRUST ********
n_politics=nordic[["polintr","polcmpl","poldcs","trstprl","trstlgl","trstplc","trstplt",
"trstprt","vote","prtyban","imbgeco",'freehms',"gincdif","stfhlth","stfedu","stfdem","stfgov"]]

#political trust counts
polintr=n_politics['polintr'].value_counts()
polcmpl=n_politics['polcmpl'].value_counts()
poldcs=n_politics['poldcs'].value_counts()
trstprl=n_politics['trstprl'].value_counts()
trstlgl=n_politics['trstlgl'].value_counts()
trstplc=n_politics['trstplc'].value_counts()
trstplt=n_politics['trstplt'].value_counts()
vote=n_politics['trstprt'].value_counts()
prtyban=n_politics['prtyban'].value_counts()
imbgeco=n_politics['imbgeco'].value_counts()
freehms=n_politics['freehms'].value_counts()
vote=n_politics['vote'].value_counts()
gincdif=n_politics['gincdif'].value_counts()
stfedu=n_politics['stfedu'].value_counts()
stfdem=n_politics['stfdem'].value_counts()
stfgov=n_politics['stfgov'].value_counts()

political_counts=pd.concat([polintr,polcmpl,poldcs,trstprl,trstlgl,vote,prtyban,imbgeco,freehms,vote,gincdif,stfedu,stfdem,stfgov], axis=1)
political_pcts=political_counts.iloc[:, 0:].apply(lambda x: (x / x.sum()*100))
poltical_pcts=political_pcts.fillna(0)

#III. DEMOGRAPHICS/Employment 
n_dem=nordic[["lvghw","edulvla","eduyrs","pdwrk","uempla","uempli","rtrd","wrkctr","uemp12m",
"edulvlmb","edulvlfb","marital"]]

lvghw=n_dem['lvghw'].value_counts()
eduyrs=n_dem['eduyrs'].value_counts()
edulvla=n_dem['edulvla'].value_counts()
pdwrk=n_dem['pdwrk'].value_counts()
uempla=n_dem['uempla'].value_counts()
uempli=n_dem['uempli'].value_counts()
rtrd=n_dem['rtrd'].value_counts()
wrkctr=n_dem['wrkctr'].value_counts() 
uemp12m=n_dem['uemp12m'].value_counts()
edulvlmb=n_dem['edulvlmb'].value_counts()
edulvlfb=n_dem['edulvlfb'].value_counts()
marital=n_dem['marital'].value_counts()

demographic_counts=pd.concat([lvghw,edulvla,eduyrs,pdwrk,uempla,uempli,rtrd,wrkctr,uemp12m,
edulvlmb,edulvlfb,marital],axis=1)
demographic_pcts=demographic_counts.iloc[:, 0:].apply(lambda x: (x / x.sum()*100))
demographic_pcts=demographic_pcts.fillna(0)

####### Other european countries ***********
#I. politics 
eur=ess
#without nordics 
eur1=ess[~(ess['cntry']=="DK") & ~(ess['cntry']=="SE") & ~(ess['cntry']=="FI") & ~(ess['cntry']=="IS") & ~(ess['cntry']=="NO")]
eur['cntry'].unique()

#comparing european poltiical system to nordic poltical system??
eur_politics=eur[["cntry","polintr","polcmpl","poldcs","trstprl","trstlgl","trstplc","trstplt",
"trstprt","vote","prtyban","imbgeco",'freehms',"gincdif","stfhlth","stfedu","stfdem","stfgov"]]

#political trust counts
polintr_eur=eur_politics.groupby('cntry')['polintr'].value_counts()
polcmpl_eur=eur_politics.groupby('cntry')['polcmpl'].value_counts()
poldcs_eur=eur_politics.groupby('cntry')['poldcs'].value_counts()
trstprl_eur=eur_politics.groupby('cntry')['trstprl'].value_counts()
trstlgl_eur=eur_politics.groupby('cntry')['trstlgl'].value_counts()
trstplc_eur=eur_politics.groupby('cntry')['trstplc'].value_counts()
trstplt_eur=eur_politics.groupby('cntry')['trstplt'].value_counts()
vote_eur=eur_politics.groupby('cntry')['vote'].value_counts()
prtyban_eur=eur_politics.groupby('cntry')['prtyban'].value_counts()
imbgeco_eur=eur_politics.groupby('cntry')['imbgeco'].value_counts()
freehms_eur=eur_politics.groupby('cntry')['freehms'].value_counts()
gincdif_eur=eur_politics.groupby('cntry')['gincdif'].value_counts()
stfedu_eur=eur_politics.groupby('cntry')['stfedu'].value_counts()
stfdem_eur=eur_politics.groupby('cntry')['stfdem'].value_counts()
stfgov_eur=eur_politics.groupby('cntry')['stfgov'].value_counts()

political_counts_eur=pd.concat([polintr_eur,polcmpl_eur,poldcs_eur,trstprl_eur,trstlgl_eur,vote_eur,prtyban_eur,imbgeco_eur,freehms_eur,vote_eur,gincdif_eur,stfedu_eur,stfdem_eur], axis=1)
political_counts_eur.reset_index(level=0,inplace=True)
political_counts_eur.reset_index(level=0,inplace=True)
political_counts_eur=political_counts_eur.rename(columns = {'level_0':'country'})
#political_counts_eur1 = political_counts_eur.groupby(['country','index']).agg({'polintr': 'sum','polcmpl':'sum','poldcs':'sum',
#'trstprl':'sum','trstlgl':'sum','vote':'sum'})

political_counts_eur1.to_csv("politics_europe.csv")
politics_eur=pd.read_csv("politics_europe.csv")

###Politically Engaged/Postive Countries 
#a. politics interest 
pol_int = political_counts_eur.groupby(['country','index']).agg({'polintr': 'sum'})
pol_int.reset_index(drop=True,inplace=False)
pol_int = pol_int.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
pol_int.reset_index(level=0,inplace=True)
pol_int.reset_index(level=0,inplace=True)
sub1= pol_int[(pol_int['index']==1) |(pol_int['index']==2)]
pol_int_score=sub1.groupby(['country'])['polintr'].agg('sum')
pol_int_score=pd.DataFrame(pol_int_score)
pol_int_score.reset_index(level=0,inplace=True)

#b. politics complicated (0-never 9-very high)
pol_cmp = political_counts_eur.groupby(['country','index']).agg({'polcmpl':'sum'})
pol_cmp.reset_index(drop=True,inplace=False)
pol_cmp = pol_cmp.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
pol_cmp.reset_index(level=0,inplace=True)
pol_cmp.reset_index(level=0,inplace=True)
#pol_cmp_score= pol_cmp[(pol_cmp['index']==1) |(pol_cmp['index']==2)]
sub2=pol_cmp[(pol_cmp['index']==1) | (pol_cmp['index']==2)]
pol_cmp_score=sub2.groupby(['country'])['polcmpl'].agg('sum')
pol_cmp_score=pd.DataFrame(pol_cmp_score)
pol_cmp_score.reset_index(level=0,inplace=True)

#c. making mind up about politics (4-5 easy)
pol_dcs = political_counts_eur.groupby(['country','index']).agg({'poldcs':'sum'})
pol_dcs.reset_index(drop=True,inplace=False)
pol_dcs = pol_dcs.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
pol_dcs.reset_index(level=0,inplace=True)
pol_dcs.reset_index(level=0,inplace=True)
sub3=pol_dcs[(pol_dcs['index']==4) | (pol_dcs['index']==5)]
pol_dcs_score=sub3.groupby(['country'])['poldcs'].agg('sum')
pol_dcs_score=pd.DataFrame(pol_dcs_score)
pol_dcs_score.reset_index(level=0,inplace=True)

#d. parliament country trust (0-no trust 10-high trust)
trst_par = political_counts_eur.groupby(['country','index']).agg({'trstprl':'sum'})
trst_par.reset_index(drop=True,inplace=False)
trst_par = trst_par.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
trst_par.reset_index(level=0,inplace=True)
trst_par.reset_index(level=0,inplace=True)
sub4=trst_par[(trst_par['index']==9) | (trst_par['index']==10)]
trst_par_score=sub4.groupby(['country'])['trstprl'].agg('sum')
trst_par_score=pd.DataFrame(trst_par_score)
trst_par_score.reset_index(level=0,inplace=True)

#e. legal system trust (0-no trust 10-high trust)
trst_lgl = political_counts_eur.groupby(['country','index']).agg({'trstlgl':'sum'})
trst_lgl.reset_index(drop=True,inplace=False)
trst_lgl = trst_lgl.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
trst_lgl.reset_index(level=0,inplace=True)
trst_lgl.reset_index(level=0,inplace=True)
sub4=trst_lgl[(trst_lgl['index']==9) | (trst_lgl['index']==10)]
trst_lgl_score=sub4.groupby(['country'])['trstlgl'].agg('sum')
trst_lgl_score=pd.DataFrame(trst_lgl_score)
trst_lgl_score.reset_index(level=0,inplace=True)

##party ban (ban parties thay wish to overthrow democracy?)-1 agree strong,2-agree,4 disagree
prtyban = political_counts_eur.groupby(['country','index']).agg({'prtyban':'sum'})
prtyban.reset_index(drop=True,inplace=False)
prtyban = prtyban.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
prtyban.reset_index(level=0,inplace=True)
prtyban.reset_index(level=0,inplace=True)
sub5=prtyban[(prtyban['index']==1) | (prtyban['index']==2)]
prtyban_score=sub5.groupby(['country'])['prtyban'].agg('sum')
prtyban_score=pd.DataFrame(prtyban_score)
prtyban_score.reset_index(level=0,inplace=True)

#gays and lesbinas live free as wish 1-strong agree, 4-disagree
freehms= political_counts_eur.groupby(['country','index']).agg({'freehms':'sum'})
freehms.reset_index(drop=True,inplace=False)
freehms = freehms.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
freehms.reset_index(level=0,inplace=True)
freehms.reset_index(level=0,inplace=True)
sub6=freehms[(freehms['index']==1) | (freehms['index']==2)]
freehms_score=sub6.groupby(['country'])['freehms'].agg('sum')
freehms_score=pd.DataFrame(freehms_score)
freehms_score.reset_index(level=0,inplace=True)

#democracy satisfied 0-ext dis, 10-sat 
stfdem= political_counts_eur.groupby(['country','index']).agg({'stfdem':'sum'})
stfdem.reset_index(drop=True,inplace=False)
stfdem= stfdem.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
stfdem.reset_index(level=0,inplace=True)
stfdem.reset_index(level=0,inplace=True)
sub7=stfdem[(stfdem['index']==9) | (stfdem['index']==10)]
stfdem_score=sub7.groupby(['country'])['stfdem'].agg('sum')
stfdem_score=pd.DataFrame(stfdem_score)
stfdem_score.reset_index(level=0,inplace=True)

#combine political dataframes 
politics=pd.merge(pol_int_score,pol_cmp_score,on="country") 
politics=pd.merge(politics,pol_dcs_score,on="country")
politics=pd.merge(politics,trst_par_score,on="country")
politics=pd.merge(politics,freehms_score,on="country")
politics=pd.merge(politics,trst_lgl_score,on="country")
politics=pd.merge(politics,stfdem_score,on="country")

#summary
corr_pol=politics.corr() 
corr_pol = corr_pol.unstack()
corr_pol = corr_pol.sort_values(kind="quicksort") #polcmpl and poldcs=0.73, trustprl and trustlgl=0.58 

politics.describe() 

#countries trust in legislative and parliament systems?
trust_countries=politics[(politics['trstprl']>4.25) & (politics['trstlgl']>9.93)] #greater than 75% --most trusting countries 
no_trust_countries=politics[(politics['trstprl']<1.99) & (politics['trstlgl']<3.11)]#least trusting countries

#countries open gay views?
countries_gay=politics[politics['freehms']>56.1] #greater than average 
countries_gay1=politics.sort_values(['country','freehms'],ascending=[True,False])
gay_values=politics.sort_values('freehms',ascending=False)['country']

#kmeans clustering******
politics_sub=politics.iloc[:,1:politics.shape[1]]
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
        
#scale dataset 
scaler=MinMaxScaler() 
scale_vars=scaler.fit_transform(politics_sub)
kmeans=KMeans(n_clusters=3,random_state=0).fit(scale_vars)
labels=kmeans.labels_
labels=pd.DataFrame(labels)
labels.columns=['Group']

politics_groups=pd.concat([politics,labels],axis=1)
group1=politics_groups[politics_groups['Group']==0]['country'] #less political tolerant 
group2=politics_groups[politics_groups['Group']==1]['country'] #turkey 
group3=politics_groups[politics_groups['Group']==2]['country'] #political tolerant 

#group1
group1_names=pd.DataFrame(group1)
group1_final=pd.merge(group1_names,politics,on="country")
g1_mean=group1_final.iloc[:,1:8].mean()
g1_mean=pd.DataFrame(g1_mean)
g1_mean=g1_mean.T 
g1_mean.to_csv("g1_mean.csv")

#group2 
group2_names=pd.DataFrame(group2)
group2_final=pd.merge(group2_names,politics,on="country")
g2_mean=group2_final.iloc[:,1:8].mean()
g2_mean=pd.DataFrame(g2_mean)
g2_mean=g2_mean.T 
g2_mean.to_csv("g1_mean.csv")

gay_tol=group2_final[group2_final['freehms']<=30]

#group3
group3_names=pd.DataFrame(group3)
group3_final=pd.merge(group3_names,politics,on="country")
g3_mean=group3_final.iloc[:,1:8].mean()
g3_mean=pd.DataFrame(g3_mean)
g3_mean=g3_mean.T 

group_final=pd.concat([g1_mean,g2_mean,g3_mean],axis=0)
group_final.to_csv("group_final_eur.csv")

###Politically 'Negative' Countries 
#a. politics interest (3-hardly,4-not at all interested)
pol_int = political_counts_eur.groupby(['country','index']).agg({'polintr': 'sum'})
pol_int.reset_index(drop=True,inplace=False)
pol_int = pol_int.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
pol_int.reset_index(level=0,inplace=True)
pol_int.reset_index(level=0,inplace=True)
sub1= pol_int[(pol_int['index']==3) |(pol_int['index']==4)]
pol_int_score=sub1.groupby(['country'])['polintr'].agg('sum')
pol_int_score1=pd.DataFrame(pol_int_score)
pol_int_score1.reset_index(level=0,inplace=True)

#b. politics complicated (4-reg comp, 5-very comp)
pol_cmp = political_counts_eur.groupby(['country','index']).agg({'polcmpl':'sum'})
pol_cmp.reset_index(drop=True,inplace=False)
pol_cmp = pol_cmp.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
pol_cmp.reset_index(level=0,inplace=True)
pol_cmp.reset_index(level=0,inplace=True)
#pol_cmp_score= pol_cmp[(pol_cmp['index']==4) |(pol_cmp['index']==5)]
sub2=pol_cmp[(pol_cmp['index']==4) | (pol_cmp['index']==5)]
pol_cmp_score=sub2.groupby(['country'])['polcmpl'].agg('sum')
pol_cmp_score1=pd.DataFrame(pol_cmp_score)
pol_cmp_score1.reset_index(level=0,inplace=True)

#c. making mind up about politics (4-5 easy)
pol_dcs = political_counts_eur.groupby(['country','index']).agg({'poldcs':'sum'})
pol_dcs.reset_index(drop=True,inplace=False)
pol_dcs = pol_dcs.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
pol_dcs.reset_index(level=0,inplace=True)
pol_dcs.reset_index(level=0,inplace=True)
sub3=pol_dcs[(pol_dcs['index']==1) | (pol_dcs['index']==2)]
pol_dcs_score=sub3.groupby(['country'])['poldcs'].agg('sum')
pol_dcs_score1=pd.DataFrame(pol_dcs_score)
pol_dcs_score1.reset_index(level=0,inplace=True)

#d. parliament country trust (0-no trust 1) 
trst_par = political_counts_eur.groupby(['country','index']).agg({'trstprl':'sum'})
trst_par.reset_index(drop=True,inplace=False)
trst_par = trst_par.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
trst_par.reset_index(level=0,inplace=True)
trst_par.reset_index(level=0,inplace=True)
sub4=trst_par[(trst_par['index']==0) | (trst_par['index']==1)]
trst_par_score=sub4.groupby(['country'])['trstprl'].agg('sum')
trst_par_score1=pd.DataFrame(trst_par_score)
trst_par_score1.reset_index(level=0,inplace=True)

#e. legal system trust (0-no,1) 
trst_lgl = political_counts_eur.groupby(['country','index']).agg({'trstlgl':'sum'})
trst_lgl.reset_index(drop=True,inplace=False)
trst_lgl = trst_lgl.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
trst_lgl.reset_index(level=0,inplace=True)
trst_lgl.reset_index(level=0,inplace=True)
sub4=trst_lgl[(trst_lgl['index']==0) | (trst_lgl['index']==1)]
trst_lgl_score=sub4.groupby(['country'])['trstlgl'].agg('sum')
trst_lgl_score1=pd.DataFrame(trst_lgl_score)
trst_lgl_score1.reset_index(level=0,inplace=True)

##party ban (ban parties thay wish to overthrow democracy?)-1 agree strong,2-agree,4 disagree
prtyban = political_counts_eur.groupby(['country','index']).agg({'prtyban':'sum'})
prtyban.reset_index(drop=True,inplace=False)
prtyban = prtyban.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
prtyban.reset_index(level=0,inplace=True)
prtyban.reset_index(level=0,inplace=True)
sub5=prtyban[(prtyban['index']==1) | (prtyban['index']==2)]
prtyban_score=sub5.groupby(['country'])['prtyban'].agg('sum')
prtyban_score1=pd.DataFrame(prtyban_score)
prtyban_score1.reset_index(level=0,inplace=True)

#gays and lesbinas live free as wish 1-strong agree, 4-disagree
freehms= political_counts_eur.groupby(['country','index']).agg({'freehms':'sum'})
freehms.reset_index(drop=True,inplace=False)
freehms = freehms.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
freehms.reset_index(level=0,inplace=True)
freehms.reset_index(level=0,inplace=True)
sub6=freehms[(freehms['index']==4) | (freehms['index']==5)]
freehms_score=sub6.groupby(['country'])['freehms'].agg('sum')
freehms_score1=pd.DataFrame(freehms_score)
freehms_score1.reset_index(level=0,inplace=True)

#democracy satisfied 0-ext dis, 10-sat 
stfdem= political_counts_eur.groupby(['country','index']).agg({'stfdem':'sum'})
stfdem.reset_index(drop=True,inplace=False)
stfdem= stfdem.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
stfdem.reset_index(level=0,inplace=True)
stfdem.reset_index(level=0,inplace=True)
sub7=stfdem[(stfdem['index']==0) | (stfdem['index']==1)]
stfdem_score=sub7.groupby(['country'])['stfdem'].agg('sum')
stfdem_score1=pd.DataFrame(stfdem_score)
stfdem_score1.reset_index(level=0,inplace=True)


#combine political dataframes ************** -----------------------------------
politics1=pd.merge(pol_int_score1,pol_cmp_score1,on="country") 
politics1=pd.merge(politics1,pol_dcs_score1,on="country")
politics1=pd.merge(politics1,trst_par_score1,on="country")
politics1=pd.merge(politics1,prtyban_score1,on="country")
politics1=pd.merge(politics1,freehms_score1,on="country")
politics1=pd.merge(politics1,trst_lgl_score1,on="country")
politics1=pd.merge(politics1,stfdem_score1,on="country")
politics1.columns=['country','pol_int_score1','pol_cmp_score1','pol_dcs_score1','trst_par_score1','prtyban_score1','freehms_score1','trst_lgl_score1','stfdem_score1']

politics.info()
politics1.info() 

#ban poltiical partyban
prtyban_score1['prtyban'].mean() 
party_ban=prtyban_score1[prtyban_score1['prtyban']>=58.04]

#no faith democracy
politics1['stfdem_score1'].describe() 
no_faith_dem=politics1[politics1['stfdem_score1']>=20]

#
####Ratios combine (positive to negative political views)
politics_final=pd.concat([politics,politics1],axis=1)
politics_final['sftdem_ratio']=politics_final['stfdem']/politics_final['stfdem_score1']
politics_final['pol_int_ratio']=politics_final['polintr']/politics_final['pol_int_score1']
politics_final['freehms_ratio']=politics_final['freehms']/politics_final['freehms_score1']
politics_final['polcmpl_ratio']=politics_final['polcmpl']/politics_final['pol_cmp_score1']
politics_final['poldcs_ratio']=politics_final['poldcs']/politics_final['pol_dcs_score1']
politics_final['trst_par_ratio']=politics_final['trstprl']/politics_final['trst_par_score1']
politics_final['trst_lgl_ratio']=politics_final['trstlgl']/politics_final['trst_lgl_score1']

country=politics_final.iloc[:,0]
politics_ratios=politics_final.iloc[:,16:23]
politics_ratios=pd.concat([country,politics_ratios],axis=1)
politics_ratios.iloc[:,1:politics_ratios.shape[1]].corr() #correlations
politics_ratios['pol_int_ratio'].describe() 

politics_ratios.sort_values('freehms_ratio',ascending=False)

politics_final.to_csv("pol_final.csv")

politics_final=politics_final.iloc[:,~politics_final.columns.duplicated()]
pol_final=politics_final.iloc[:,1:politics.shape[1]]
pol_final.corr()

####### demographics *********************************************************
eur_dems=eur[["cntry","lvghw","edulvla","eduyrs","pdwrk","uempla","uempli","rtrd","wrkctr","uemp12m",
"edulvlmb","edulvlfb","marital"]]

#demographics count
lvghw_eur=eur_dems.groupby('cntry')['lvghw'].value_counts()
edulvla_eur=eur_dems.groupby('cntry')['edulvla'].value_counts()
eduyrs_eur=eur_dems.groupby('cntry')['eduyrs'].value_counts()
pdwrk_eur=eur_dems.groupby('cntry')['pdwrk'].value_counts()
uempla_eur=eur_dems.groupby('cntry')['uempla'].value_counts()
uempli_eur=eur_dems.groupby('cntry')['uempli'].value_counts()
uemp12m_eur=eur_dems.groupby('cntry')['uemp12m'].value_counts()
rtrd_eur=eur_dems.groupby('cntry')['rtrd'].value_counts()
wrkctr_eur=eur_dems.groupby('cntry')['wrkctr'].value_counts()
edulvlmb_eur=eur_dems.groupby('cntry')['edulvlmb'].value_counts()
edulvlfb_eur=eur_dems.groupby('cntry')['edulvlfb'].value_counts()
marital_eur=eur_dems.groupby('cntry')['marital'].value_counts()

dem_counts_eur=pd.concat([lvghw_eur,edulvla_eur,eduyrs_eur,pdwrk_eur,uempla_eur,uempli_eur,rtrd_eur,wrkctr_eur,uemp12m_eur,
edulvlmb_eur,edulvlfb_eur,marital_eur], axis=1)
dem_counts_eur.reset_index(level=0,inplace=True)
dem_counts_eur.reset_index(level=0,inplace=True)
dem_counts_eur=dem_counts_eur.rename(columns = {'level_0':'country'})


#10/25/18 
###Demographics------------------
#a. living with partner 
lvghw = dem_counts_eur.groupby(['country','index']).agg({'lvghw': 'sum'})
lvghw.reset_index(drop=True,inplace=False)
lvghw = lvghw.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
lvghw.reset_index(level=0,inplace=True)
lvghw.reset_index(level=0,inplace=True)
sub1= lvghw[lvghw['index']==1]
lvghw_score=sub1.groupby(['country'])['lvghw'].agg('sum')
lvghw_score=pd.DataFrame(lvghw_score)
lvghw_score.reset_index(level=0,inplace=True)

#b.highest level of education completed 4/5 (post-secondary/tertiary edu)
edulvla = dem_counts_eur.groupby(['country','index']).agg({'edulvla': 'sum'})
edulvla.reset_index(drop=True,inplace=False)
edulvla = edulvla.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
edulvla.reset_index(level=0,inplace=True)
edulvla.reset_index(level=0,inplace=True)
sub2= edulvla[(edulvla['index']==4) |(edulvla['index']==5) ]
edulvla_score=sub2.groupby(['country'])['edulvla'].agg('sum')
edulvla_score=pd.DataFrame(edulvla_score)
edulvla_score.reset_index(level=0,inplace=True)

#c. looking for work past 12 months work 1-yes, 2-no
uemp12m = dem_counts_eur.groupby(['country','index']).agg({'uemp12m': 'sum'})
uemp12m.reset_index(drop=True,inplace=False)
uemp12m = uemp12m.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
uemp12m.reset_index(level=0,inplace=True)
uemp12m.reset_index(level=0,inplace=True)
sub3= uemp12m[uemp12m['index']==2] 
uemp12m_score=sub3.groupby(['country'])['uemp12m'].agg('sum')
uemp12m_score=pd.DataFrame(uemp12m_score)
uemp12m_score.reset_index(level=0,inplace=True)

#d. last 7 days (unemployed actively looking for job?) 0-not marked, 1-marked
unemp = dem_counts_eur.groupby(['country','index']).agg({'uempla': 'sum'})
unemp.reset_index(drop=True,inplace=False)
unemp =unemp.groupby(level=0).apply(lambda x:
                                                 100 * x / float(x.sum()))
unemp.reset_index(level=0,inplace=True)
unemp.reset_index(level=0,inplace=True)
sub4= unemp[unemp['index']==1] 
unemp_score=sub4.groupby(['country'])['uempla'].agg('sum')
unemp_score=pd.DataFrame(unemp_score)
unemp_score.reset_index(level=0,inplace=True)

#combine dataframes 
dem1=pd.merge(lvghw_score,edulvla_score,on="country")
dem2=pd.merge(dem1,uemp12m_score,on="country")
dem3=pd.merge(dem2,unemp_score,on="country")

dem3.to_csv("dem.csv")

dem3['uemp12m'].corr(dem3['uempla'])
dem3.sort_values('uempla')
dem3['uempla'].mean() 


#summary stats 
#a. education
edu_rank=dem2.sort_values("edulvla",ascending=False) 
dem2['edulvla'].mean() 
dem2['uemp12m'].mean()
dem2['edulvla'].corr(dem2['uemp12m']) #0.26
dem2['lvghw'].corr(dem2['uemp12m'])]
##
high_edu_high_uemp=dem2[(dem2['edulvla']>27.1) & (dem2['uemp12m']>15)]

#b. unemployed
dem2['uemp12m'].mean() 
umemp=dem2[dem2['uemp12m']>13.035]
umemp.sort_values('uemp12m')

#c. household
dem2['lvghw'].describe() 
high_live=dem2[dem2['lvghw']>0]
high_live['lvghw'].mean() 
high_live.sort_values('lvghw')

###years in education numbers
eduyrs_eur1=pd.DataFrame(eduyrs_eur)
eduyrs_eur1.reset_index(level=0,inplace=True)
eduyrs_eur1.columns=['cntry','edy_years_count']
eduyrs_eur1.reset_index(inplace=True)
eduyrs_eur1['sum_edu_years']=eduyrs_eur1['eduyrs']*eduyrs_eur1['edy_years_count']
avg_edu=eduyrs_eur1.groupby('cntry')['sum_edu_years'].mean()

###combine demographic and politics
dem_combo=pd.merge(politics_final,dem2,on="country") 
dem_combo.corr() 
dem_combo['uemp12m'].corr(dem_combo[''])

#averages 
dem_combo_avg=dem_combo.iloc[:,1:dem_combo.shape[1]].mean() 
dem_combo_avg=pd.DataFrame(dem_combo_avg) 
dem_combo_avg.reset_index(level=0,inplace=True)
dem_combo_avg.columns=['index','average']
dem_combo_avg.to_csv("avg.csv")


