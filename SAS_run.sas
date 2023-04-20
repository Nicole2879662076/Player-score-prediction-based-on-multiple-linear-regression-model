PROC IMPORT OUT= WORK.BOXT 
            DATAFILE= "C:\Users\wangsiyuan\Desktop\train.xlsx" 
            DBMS=EXCEL REPLACE;
     RANGE="train$"; 
     GETNAMES=YES;
     MIXED=NO;
     SCANTEXT=YES;
     USEDATE=YES;
     SCANTIME=YES;
RUN;

#Plot eg.
proc gplot data=Fifatrain;
plot overall_rating*age;
symbol value = circle color = black;
run;

proc gplot data=Fifatrain;
plot overall_rating*age=body_type;
symbol1 value = plus color = blue;
symbol2 value = dot color = black;
symbol3 value = plus color = red;
run;

#Corr eg.
proc corr data=Fifatrain;
title "Correlation between age and overall_rating";
var overall_rating age;
run;

#Forward selection
PROC REG DATA = Fifa;
MODEL overall_rating = age height_cm weight_kgs value_euro finishing 
dribbling volleys acceleration crossing heading_accuracy Z1 Z2 
/selection = forward slentry=0.1 ;
RUN;

#Regression estimate eg.
PROC REG DATA = Fifa;
MODEL overall_rating = age height_cm weight_kgs value_euro finishing 
dribbling acceleration crossing / XPX I COVB;
TITLE "Regression eastimation";
RUN;

#QQplot
proc reg data = Fifa plots = qqplot;
model overall_rating = age height_cm weight_kgs log_of_value 
dribbling acceleration ;
output out = res r=r;
run;
quit;
proc reg data = res normal;
var r;
run;

#BoxCoxplot
proc transreg details data = Fifa;
model boxcox(overall_rating/ lambda=-2 to 2 by 0.01) = identity(age) 
identity(height_cm) identity(weight_kgs) identity(log_of_value) 
identity(dribbling) identity(acceleration);
run;

#Collinearity
PROC REG DATA = CL;
MODEL overall_rating = 
age log_value_euro finishing / COLLIN COLLINOINT;
RUN;

