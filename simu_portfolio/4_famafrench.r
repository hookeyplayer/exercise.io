ff <- read.csv("famafrench.csv", head = TRUE, sep = ",")
ffregrs = cbind(ff$IFX.Rf,ff$DTE.Rf, ff$BMW.Rf, ff$BAYN.Rf, 
                ff$ALV.Rf, ff$ADIDAS.Rf)
# names(ffregrs)<-c("ifx", "dte", "bmw", 'bayn', "alv", "adidas")
# str(ffregrs)
fit = lm(cbind(ff$ALV.Rf, ff$DTE.Rf, ff$BAYN.Rf) ~ ff$SMB + ff$HML + ff$Mkt.Rf)
fit
cor(fit$residuals)
covRob(fit$residuals,cor=T)
cor.test(fit$residuals[,1], fit$residuals[,2])
cor.test(fit$residuals[,1], fit$residuals[,3])
cor.test(fit$residuals[,2], fit$residuals[,3])

pdf("FamaFrenchResidualsPairs.pdf",width=6,height=5)  ## Figure 18.8
pairs(fit$residuals)
graphics.off()

pdf("FamaFrenchPairs.pdf",width=8,height=8) 
pairs(cbind(ff$ALV.Rf, ff$DTE.Rf, ff$BAYN.Rf, ff$SMB, ff$HML, ff$Mkt.Rf))
graphics.off()
