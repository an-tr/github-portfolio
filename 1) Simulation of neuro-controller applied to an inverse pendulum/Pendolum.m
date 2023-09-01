clc
close all
clear all
%run = 1;

%Forza = +-10; %output rete azione
%mc = 1.0; %massa carrello 
%mp = 0.1; % massa palo
%l = 0.5; % distanza centro di massa
g = 9.8; % accelerazione 
%ts = 0.02;%timestep

%INIZIO MENU
sib=inputdlg('inserire il valore della forza che si vuole applicare al carrello (es: +-10) ');
Forza=str2num(sib{1});
sib=inputdlg('Inserire il valore della massa del carrello ');
mc=str2num(sib{1});
sib=inputdlg('Inserire il valore della massa del pendolo');
mp=str2num(sib{1});
sib=inputdlg('Inserire la distanza dal centro di massa del pendolo al pivot ');
l=str2num(sib{1});
sib=inputdlg('inserire il valore del time step utilizzato nelle equazioni di eulero');
ts=str2num(sib{1});
sib=inputdlg('ACTION NETWORK : inserire il valore di ro ( learning rate for output units). [1.0]');
ro=str2num(sib{1});
sib=inputdlg('ACTION NETWORK : inserire il valore di roh ( learning rate for hidden units). [0.2]');
roh=str2num(sib{1});
sib=inputdlg('EVALUATION NETWORK : inserire il valore di beta ( learning rate for output units). [0.2]');
beta=str2num(sib{1});
sib=inputdlg('EVALUATION NETWORK : inserire il valore di betah ( learning rate for hidden units). [0.05]');
betah=str2num(sib{1});
sib=inputdlg('EVALUATION NETWORK : inserire il valore di gamma (discount rate: 0 <= gamma < 1).  [0.9]');
gamma=str2num(sib{1});
sib=inputdlg('Inserire il numero di time step (tmax)');
tmax=str2num(sib{1});
sib=inputdlg('Inserire il limite inferiore per teta (angolo del pendolo) in radianti ');
limiteinferioreteta=str2num(sib{1});
sib=inputdlg('Inserire il limite superiore per teta (angolo del pendolo) in radianti ');
limitesuperioreteta=str2num(sib{1});
sib=inputdlg('Inserire il limite inferiore per h (posizione del carrello) in metri ');
limiteinferioreh=str2num(sib{1});
sib=inputdlg('Inserire il limite superiore per h (posizione del carrello) in metri ');
limitesuperioreh=str2num(sib{1});
%FINE MENU


%ro = 1.0;
%roh = 0.2;
%beta = 0.2;
%betah = 0.05;
%gamma = 0.9;
%tmax =9000000;
somma = 0;
somma1 = 0;
somma2 = 0;
somma3 = 0;
somma4 = 0;
somma5 = 0;
somma6 = 0;
somma7 = 0;
somma8 = 0;
somma9 = 0;
somma10 = 0;
somma11 = 0;
somma12 = 0;
sig = zeros([1,5]);
sig1 = zeros([1,5]);
sig2 = zeros([1,5]);
sig3 = zeros([1,5]);
sig4 = zeros([1,5]);
% la modifica che ho fatto è passare da rand a randn
h = rand([1,tmax]);
dh = rand([1,tmax]);
teta = rand([1,tmax]);
dteta = rand([1,tmax]);
DtDt = zeros([1,tmax]); % derivata seconda di teta
DhDh = zeros([1,tmax]); % derivata seconda di h 

%input alla rete 
x1 = zeros([1,tmax]);
x2 =  zeros([1,tmax]);
x3 =  zeros([1,tmax]);
x4 =  zeros([1,tmax]);
x5 = zeros([1,tmax]);
X = zeros([1,5,tmax]);

r = zeros([1,tmax]); %segnale di fallimento
y = zeros([1,5,tmax]); % output unità nascoste
yt = zeros([1,5,tmax]);
z = zeros([1,5,tmax]); % action
v =  zeros([1,tmax]); % evaluation 
vt =  zeros([1,tmax]);
p =  zeros([1,tmax]); % probabilità
q = zeros([1,tmax]); 
er = zeros([1,tmax]); %AHC

%matrici dei pesi ( inizialmente ipostati a avlori casuali compresi tra -0.1 e 0.1)
n=5;
inf = -0.1;
sup = 0.1;
A = inf+(sup-inf).*rand(n,n,tmax); % matrice di valori casuali compresi [-0.1,0.1]
B = inf+(sup-inf).*rand(1,n,tmax);
C = inf+(sup-inf).*rand(1,n,tmax);
%metrice dei pesi per action network
D= inf+(sup-inf).*rand(n,n,tmax);
E= inf+(sup-inf).*rand(1,n,tmax);
F= inf+(sup-inf).*rand(1,n,tmax);


massimo=tmax-1;
parziale= massimo/12;
k = 1; % contatore fallimenti 
PP=[]
plottare =1;
parziali =0;
ultimoerrore = 0;


x1(1,1) = (1/4.8)*(h(1,1)+2.4);
    x2(1,1) = (1/3)*(dh(1,1)+1.5);
    x3(1,1) = (1/0.42)*(teta(1,1)+0.21);
    x4(1,1) = (1/4)*(dteta(1,1)+2);
    x5 = 0.5; %costate bias

    X(1,1,1)=x1(1,1);
    X(1,2,1)=x2(1,1);
    X(1,3,1)=x3(1,1);
    X(1,4,1)=x4(1,1);
    X(1,5,1)=x5;

    %Per registrare l'animazione del pendolo 
    %vidObj = VideoWriter('AltroFile','Uncompressed AVI');
    %open(vidObj)

for tmax = 1: massimo 

    % 1 : calcola la valutazione dello stato corrente 

    

    
        %calcolo la valutazione dello stato corrente nel caso iniziale
        %vt(t,t)
         for i = 1:5
            somma = 0;
            for j = 1:5
                somma = somma + A(i,j,tmax)*X(1,j,tmax);
            end
            sig(1,i) = sigmoide(somma);
            yt(1,i,tmax) = sig(1,i);
        end
        somma1=0;
        somma2=0;
        for i = 1:5
            somma1 = somma1 + B(1,i,tmax)*X(1,i,tmax);
            somma2 = somma2 + C(1,i,tmax)*yt(1,i,tmax);
        end
        vt(1,tmax) = somma1+somma2;

   
    % 2,3  :  calcolo probabilita d'azione e faccio l'azione

     for i = 1:5
            somma11 = 0;
            for j = 1:5
                somma11 = somma11 + D(i,j,tmax)*X(1,j,tmax);
            end
            sig4(1,i) = sigmoide(somma11);
            z(1,i,tmax) = sig4(1,i);
     end

        %probabilità
        somma12 = 0;
        for i = 1:5
            somma12 = somma12 + E(1,i,tmax)*X(1,i,tmax) + F(1,i,tmax)*z(1,i,tmax);
        end
        p(1,tmax) = sigmoide(somma12);

        if rand(1) < p(1,tmax)
          q(1,tmax) = 1;
       else
          q(1,tmax) = 0;
       end

       if q(1,tmax) == 1
          Forza = 10;
       elseif q(1,tmax) == 0
        Forza = -10;
       end
       
       
       
    
    senteta = sin(teta(1,tmax));
    costeta = cos(teta(1,tmax));
    num = g*senteta+costeta*((-Forza - (mp*l)*(dteta(1,tmax)^2)*senteta)/(mc+mp));
    den = l*((4/3)-((mp*costeta^2)/(mc+mp)));
    DtDt(1,tmax)= num/den;
    DhDh(1,tmax)=(Forza+mp*l*((dteta(1,tmax)^2)*senteta-DtDt(1,tmax)*costeta))/(mc+mp);
    
    
   h(1,tmax+1) = h(1,tmax)+ts*dh(1,tmax);
   dh(1,tmax+1) = dh(1,tmax)+ts*DhDh(1,tmax);
   teta(1,tmax+1) = teta(1,tmax)+ts*dteta(1,tmax);
   dteta(1,tmax+1) = dteta(1,tmax)+ts*DtDt(1,tmax);

   

 % limiteinferioreteta = -0.21;
 % limitesuperioreteta = 0.21;
 %  limiteinferioreh = -2.4;
 %  limitesuperioreh = 2.4;
   

    if ((limiteinferioreteta < teta(1,tmax+1) ) && (teta(1,tmax+1) < limitesuperioreteta)) && ((limiteinferioreh< h(1,tmax+1)) && (h(1,tmax+1) < limitesuperioreh))
    
       r(1,tmax+1) = 0;
    else
       
      r(1,tmax+1) = -1;
    end

   x1(1,tmax+1) = (1/4.8)*(h(1,tmax+1)+2.4);
    x2(1,tmax+1) = (1/3)*(dh(1,tmax+1)+1.5);
    x3(1,tmax+1) = (1/0.42)*(teta(1,tmax+1)+0.21);
    x4(1,tmax+1) = (1/4)*(dteta(1,tmax+1)+2);
    x5 = 0.5; %costate bias

    X(1,1,tmax+1)=x1(1,tmax+1);
    X(1,2,tmax+1)=x2(1,tmax+1);
    X(1,3,tmax+1)=x3(1,tmax+1);
    X(1,4,tmax+1)=x4(1,tmax+1);
    X(1,5,tmax+1)=x5;


   % 4  :  calcolo v stato successivo v(t,t+1)

   for i = 1:5
            somma5 = 0;
            for j = 1:5
                somma5 = somma5 + A(i,j,tmax)*X(1,j,tmax+1);
            end
            sig2(1,i) = sigmoide(somma5);
            y(1,i,tmax) = sig2(1,i);
   end
        somma6=0;
        somma7=0;
        for i = 1:5
            somma6 = somma6 + B(1,i,tmax)*X(1,i,tmax+1);
            somma7 = somma7 + C(1,i,tmax)*y(1,i,tmax);
        end
        v(1,tmax) = somma6+somma7;

        % 5 : calcolo la differenza temporale er(tmax +1)

        if(r(1,tmax+1) == -1)
        er(1,tmax+1) = r(1,tmax+1)-vt(1,tmax);
       else
        er(1,tmax+1)= r(1,tmax+1)+gamma*v(1,tmax)-vt(1,tmax);
        end

        % 6  : aggiornamnto pesi
        %aggiorno i pensi della rete di valutazione
       for i = 1:5
        for j  = 1:5
            
           csign = sign(C(1,i,tmax));
           A(i,j,tmax+1) = A(i,j,tmax)+ betah*er(tmax+1)*yt(1,i,tmax)*(1-yt(1,i,tmax)*csign*X(1,j,tmax));
        end 
        B(1,i,tmax+1) = B(1,i,tmax)+beta*er(1,tmax+1)*X(1,i,tmax);
        C(1,i,tmax+1) = C(1,i,tmax)+ beta*er(1,tmax+1)*yt(1,i,tmax);
       end

       %aggiorno i pesi della rete d'azione
       for i = 1:5
         for j = 1:5
             fsign = sign(F(1,i,tmax));
        D(i,j,tmax+1) = D(i,j,tmax)+roh*er(1,tmax+1)*z(1,i,tmax)*(1-z(1,i,tmax)*fsign*(q(1,tmax)-p(1,tmax))*X(1,j,tmax));
        %D(i,j,tmax) = D(i,j,tmax-1)+roh*er(tmax).*z(i,tmax-1).*(1-z(i,tmax-1).*F(1,i,tmax-1).*(q(tmax-1)-p(tmax-1)).*X(1,j,tmax-1));
         end
         E(1,i,tmax+1)=E(1,i,tmax)+ro*er(1,tmax+1)*(q(1,tmax)-p(1,tmax))*X(1,i,tmax);
         F(1,i,tmax+1)=F(1,i,tmax)+ro*er(1,tmax+1)*(q(1,tmax)-p(1,tmax))*z(1,i,tmax);
       end

       ultimoerrore= ultimoerrore + 1;

       % 7  : se fallimento occorre resettare step counter a zero
       if (r(tmax+1) == -1)
    ap = -0.1;
    bp = 0.1;
    hp = -0.1;
    kp = 0.1;
    tinf = -0.1;
    tsup = 0.1;

  
    h(1,tmax+1) = hp + (kp-hp)*rand(1);
   dh(1,tmax+1) = ap + (bp-ap)*rand(1);
   teta(1,tmax+1) = tinf + (tsup-tinf)*rand(1);
   dteta(1,tmax+1) = ap + (bp-ap)*rand(1);

    %h(1,tmax+1) = rand(1)*0.1;
   %dh(1,tmax+1) = rand(1)*0.1;
   %teta(1,tmax+1) = rand(1)*0.1;
   %dteta(1,tmax+1) = rand(1)*0.1;

   x1(1,tmax+1) = (1/4.8)*(h(1,tmax+1)+2.4);
    x2(1,tmax+1) = (1/3)*(dh(1,tmax+1)+1.5);
    x3(1,tmax+1) = (1/0.42)*(teta(1,tmax+1)+0.21);
    x4(1,tmax+1) = (1/4)*(dteta(1,tmax+1)+2);
    x5 = 0.5; %costate bias

    X(1,1,tmax+1)=x1(1,tmax+1);
    X(1,2,tmax+1)=x2(1,tmax+1);
    X(1,3,tmax+1)=x3(1,tmax+1);
    X(1,4,tmax+1)=x4(1,tmax+1);
    X(1,5,tmax+1)=x5;

    k=k+1;
    ultimoerrore=0;
   % fprintf('%s\t%s\n','k','t  ');
    %fprintf('%d\t%1.1f\n',k,tmax);
    
    

       end

       %%plot
    if (plottare==1 && tmax>massimo-10000)
       subplot(2,1,1)
    hold off
    plot([h(1,tmax),h(1,tmax)+sin(teta(1,tmax))],[0,cos(teta(1,tmax))],'-k','LineWidth',1)
    hold on
    plot(h(1,tmax),0,'sr','MarkerSize',10)
    xlim([-2.4,2.4])
    ylim([-2,2])
    subplot(2,1,2)
    x=[h(1,tmax) dh(1,tmax) teta(1,tmax) dteta(1,tmax)];

   % ff=getframe(gcf);
    
    PP=[PP,x'];
    plot(PP')
    legend('h','dh','teta','dteta')
%     if mod(T,100)==0
    drawnow
    
    %per registrazione animazione pendolo
    % frame = getframe(gcf); %get frame
    %writeVideo(vidObj, frame);




    
    end
        
    

       %print
    %disp(A(:,:,tmax));
   % fprintf('%s\t%s %s\t%s %s\t%s \n','k','t  ','fallimento ','teta(tmax)','forza  ','dteta(tmax)');
    %fprintf('%d\t%1.1f %d\t%1.1f %d\t%1.1f \n',k,tmax,r(1,tmax),teta(1,tmax),Forza, dteta(1,tmax));
    %disp(A(:,:,tmax))

    if(parziali == 1)
    
    if (tmax==parziale)
        errori1=k;
    end
    if (tmax==parziale*2)
        errori2=k-errori1;
    end
    if (tmax==parziale*3)
        errori3=k-errori2-errori1;
    end
    if (tmax==parziale*4)
        errori4=k-errori3-errori2-errori1;
    end
    if (tmax==parziale*5)
        errori5=k-errori4-errori3-errori2-errori1;
    end
    if (tmax==parziale*6)
        errori6=k-errori5-errori4-errori3-errori2-errori1;
    end
    if (tmax==parziale*7)
        errori7=k-errori6-errori5-errori4-errori3-errori2-errori1;
    end
    if (tmax==parziale*8)
        errori8=k-errori7-errori6-errori5-errori4-errori3-errori2-errori1;
    end
    if (tmax==parziale*9)
        errori9=k-errori8-errori7-errori6-errori5-errori4-errori3-errori2-errori1;
    end
    if (tmax==parziale*10)
        errori10=k-errori9-errori8-errori7-errori6-errori5-errori4-errori3-errori2-errori1;
    end
    if (tmax==parziale*11)
        errori11=k-errori10-errori9-errori8-errori7-errori6-errori5-errori4-errori3-errori2-errori1;
    end
    if (tmax==parziale*12)
        errori12=k-errori11-errori10-errori9-errori8-errori7-errori6-errori5-errori4-errori3-errori2-errori1;
    end

    end


end
%per registrazione animazione pendolo
%close(vidObj)

if(parziali == 1)
disp('errori fino a');
disp(parziale);
disp(errori1);
disp('errori fino a');
disp(parziale*2);
disp(errori2);
disp('errori fino a');
disp(parziale*3);
disp(errori3);
disp('errori fino a');
disp(parziale*4);
disp(errori4);
disp('errori fino a');
disp(parziale*5);
disp(errori5);  
disp('errori fino a');
disp(parziale*6);
disp(errori6);

disp('errori fino a');
disp(parziale*7);
disp(errori7);
disp('errori fino a');
disp(parziale*8);
disp(errori8);
disp('errori fino a');
disp(parziale*9);
disp(errori9);
disp('errori fino a');
disp(parziale*10);
disp(errori10);
disp('errori fino a');
disp(parziale*11);
disp(errori11);
disp('errori fino a');
disp(parziale*12);
disp(errori12);

end
%disp('RUN')
%disp(run)

disp('ultimo errore e stato tot cicli fa');
disp(ultimoerrore);

disp('errori totali');
disp(k);

disp('tempo medio senza errori');
tmedio=massimo/k;
disp(tmedio);

%run = run+1;
 

