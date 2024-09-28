from scipy.stats import t
import numpy.matlib as mb
import numpy.linalg as lg
import ipywidgets as widgets
import math as mt
import numpy as np
import pandas as pd
import re

def erroMedicao(VVC, xi):
  n = np.size(xi,0) # n - Tamanho das amostas
  mVVC = mb.repmat(VVC,n,1) # Replica o vetor coluna VVc em n linhas
  em = (xi - mVVC)
  emMaxAbs = np.max(abs(em),0).T
  return (emMaxAbs)

def erroSistematico(VVC, xi):
  vm = np.mean(xi,0) # Média aritmética de cada linha
  return ((vm - VVC).T) # Erro sistemático ou Tendência

def erroAleatorio(xi):
  n = np.std(xi,0,ddof=1)
  return (n.T)

def histerese(xiAvanco,xiRecuo):
  vmAvanco = np.mean(xiAvanco,0) # Média aritmética em avanço.
  vmRecuo = np.mean(xiRecuo,0) # Média aritmética em recuo | retorno.
  hist = abs(vmAvanco-vmRecuo)
  histMax = np.max(hist,0)
  return (np.asmatrix(hist).T)

def linearidade(VVC, xi):
  tam = np.size(VVC,1) # Quantidade de valores analisados
  VVC = VVC.T
  vm = np.mean(xi,0).T # Média aritmética de cada linha
  # Calcula a reta com menor erro em relação as medidas - MMQ
  mt = np.concatenate((vm, np.ones((tam,1))),1)
  x = lg.inv(mt.T @ mt)
  y = mt.T @ VVC
  coef = x @ y # Faz a linearização com os dados
  eVVC = coef[0,0]*vm+coef[1,0] # VVC estimado
  el = abs(VVC - eVVC)
  elMax = np.max(el, 0)
  return (el)

def repetitividade(xi):
  return(np.std(xi,0,ddof=1).T) # Calcula o Desvio Padrão

def incertezaPadraoTipoA(st, n): # Incerteza Padrão do Tipo A
  return (np.asmatrix(st/mt.sqrt(n)))

def incertezaPadraoTipoB(uTB,caracteristicasPadrao): #Incerteza Padrão do Tipo B
  desc = uTB[0]
  y = uTB[1]
  tipo = re.search(r"^([^ |\(])+",desc)
  if tipo!=None:
    desc = tipo.group(0)
  if desc == 'Res':
    resp = y/(2*mt.sqrt(3))
  elif tipo[0] == 'Deriva':
    resp = y/mt.sqrt(3)
  elif tipo[0] == 'Lin':
    resp = y/mt.sqrt(3)
    #resp = zeros(size(y,1),1)
  elif tipo[0] == 'Hist':
    resp = y/(2*mt.sqrt(3))
  else: # "Quando for Incerteza - U"
    try:
      resp = y/caracteristicasPadrao['k'] # fatorAbrang
    except:
      resp = y
  return (resp)

def incertezaCombinada(y): # Cálculo da Incerteza Combinada
  return(np.sqrt(np.sum(np.square(y), axis=1)))

def grauLiberdadeEfetivo(uc,uTA,n,uTB,caracteristicasPadrao): # CÁLCULO DO GRAU DE LIBERDADE EFETIVO
  numerador = np.power(uc,4)
  veff = mb.repmat((np.asmatrix(caracteristicasPadrao['veff'])).T,1,np.size(uTB,1))
  va = mb.repmat(np.asmatrix([n-1]),np.size(uTA,0),1) # Grau de Liberdade
  denominador = (np.power(uTA,4)/va)+np.sum(np.power(uTB,4)/veff, axis=1)
  vefF = numerador/denominador # GRAU DE LIBERDADE EFETIVO
  return(vefF)

def fatorAbrangencia(nivelConfianca,veff):
  k=t.ppf(1-((1-nivelConfianca/100)/2),veff)
  return(k)

def incertezaExpandida(uc,k):#Cálculo da Incerteza Expandida
  ue = np.multiply(uc,k)
  return (ue)

def caractEstatico(caracteristicasPadrao, uTB, nivelConfiancaDesejado, VVC, xi, xi_avanco, xi_atraso):
  em = erroMedicao(VVC, xi)
  es = erroSistematico(VVC, xi)
  ea = erroAleatorio(xi)
  rep = repetitividade(xi)
  lin = linearidade(VVC, xi)
  hist = histerese(xi_avanco,xi_atraso)

  uTA_padrao = incertezaPadraoTipoA(rep,np.size(xi,0))
  a = (np.asmatrix(np.array([incertezaPadraoTipoB(x,caracteristicasPadrao) for x in uTB]))).T
  b = incertezaPadraoTipoB(('Lin',lin),caracteristicasPadrao)
  c = incertezaPadraoTipoB(('Hist',hist),caracteristicasPadrao)
  uTB_padrao = np.concatenate((a, b, c), 1)
  uc = incertezaCombinada(np.concatenate((uTA_padrao, uTB_padrao),1))
  veff = grauLiberdadeEfetivo(uc,uTA_padrao,np.size(xi,0),uTB_padrao,caracteristicasPadrao)
  k = fatorAbrangencia((np.asmatrix(nivelConfiancaDesejado)).T,veff)
  ue = incertezaExpandida(uc,k)

  desc = ["EM","ES","EA","Rep","Hist","ELin","uTA (Rep_p)"]+[x[0]+"_p" for x in uTB]+["Lin_p",'Hist_p',"uC","Veff","k","uE"]
  data = np.concatenate((em, es, ea, rep, hist, lin, uTA_padrao, uTB_padrao, uc, veff, k, ue), 1)

  return(pd.DataFrame(data=data, columns=desc))

caracteristicasPadrao = {'k': np.matrix([2, 2, 2, 2]),
                         'veff': np.matrix([np.Inf, np.Inf, np.Inf, np.Inf])}

uTB = [('Res',np.matrix([0.1, 0.1, 0.1, 0.1])),
       ('Res (p)',np.matrix([0.01, 0.01, 0.01, 0.01])),
       ('u (p)',np.matrix([0.001, 0.001, 0.001, 0.001])),
       ('Deriva (p)',np.matrix([0.002, 0.002, 0.002, 0.002]))]

nivelConfiancaDesejado = np.matrix([95.45,95.45,95.45,95.45])

VVC = np.matrix(  [5.000,10.000,20.000,40.000])       #valor nominal

xi = np.matrix([  [4.8482, 9.8763, 19.9071, 39.8279], #leitura 1 (por coluna)
                  [4.9284, 9.8646, 19.85773, 39.8979], #leitura 2
                  [4.9005, 9.9253, 19.8966, 39.6242], #leitura 3
                  [4.9351, 9,9186, 19.90882, 39.9042]]) #leitura 4

caractEstatico(caracteristicasPadrao, uTB, nivelConfiancaDesejado, VVC, xi, np.ones((1,np.size(xi,1))), np.ones((1,np.size(xi,1))))