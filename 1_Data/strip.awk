#BEGIN{
#    printf("%s\n","Running awk script strip.awk")
#}
{
    if($1 ~ />/ && $1 !~ />S/){
        if($5 ~ /Group/){
            printf("%s %s %.7f %s %.7f \t %s %.5f %s %.5f\n",$4, "Amplitude:", $10, "+/-", $11, "Phase:", $8, "+/-", $9)
#            printf("%s %s\n","Group:", $0)
        }
        else{
            printf("%s %s %.7f %s %.7f \t %s %.5f %s %.5f\n",$4, "Amplitude:", $9, "+/-", $10, "Phase:", $7, "+/-", $8)
#            printf("%s %s\n","No Group:", $0)
        }
    }
    if($1 ~ /"/){
        printf("\n%s %s %s %f\n","Hyperparameter", $2, "is", $4)
    }
}
#END{
#    printf("%s\n",$0)
#}
#awk '{if($1 ~ /"/){printf("\n%s %s %s %f\n","Hyperparameter", $2, "is", $4)}}' < TH.results >> TH.phases
#echo "########################################################" >> TH.phases
