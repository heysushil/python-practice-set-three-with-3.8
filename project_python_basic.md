# Student class admission and result project using Python basic concept:

> Note: Ye project pyhton basic concpts ka use kar ke bana hai.
> Note: Yaha par aapko fucntion ka hi use karna hai. Otherwise aapka kam nahi ho payega.

## Student admistion section

1. Sabse pahle student ka registration karna hai. Jisme ki following details student se leni hai:
    1. Student Personal details:
        1. student first name
        1. student middle name
        1. student last name
        1. student father's name
        1. student mother's name
        1. student mobile number
        1. student email id
        1. student address
    1. Student Class details:
        1. student roll number
        1. student class name
        1. student subject 1
        1. student subject 2
        1. student subject 3
        1. student subject 4
    >Note: Studnet registration part me personal and class realated data ko store karne ke liye dict ka use kiya ja sakta hai:
        
        mydata = {
            'personal' : {
                'stuentName' : input('Enter name: '),
                .
                .
                .
                .
            },
            'class' : {
                'classname' : input('Enter class: ),
            }
        }
1. Dhyan rahe ki:
    1. ye sari value aap jis form me store karna caho kar sakte ho.
    1. Yad rahe student ka personal aur class details seprate rahe taki aage class detail ka use kar ke studen ko subject wise marks de sako.

> Note: Is case me condtion ka use karna hai aur a/s/m mese kisi bhi ko enter karte hi use us fucntion me pahoch jaye.

## Studens registration success:

1. Student ka registration hone ke baad sari details show karani hai.
1. Dhyan rahe ki details 2 section me hoga personal and class. Is ke liye multiline string ka use karoge.
1. Last me agar registration successful rahta hain then user ko message show karna hai ki:
    1. enter a (again) again kisi aur student registration ke liye
    1. enter m (marks) student marks dene ke liye
    1. enter e (exit)

## Student marks section:

1. Student ke subject waise number enter karenge.
1. Yaha par student ka percentag nikalna hai using total number. Formula (SubjectWiseNumbers / totalNumbrs * 100)

## Student ka resutl show karna:

1. Student ke percantage ki hisab se student pass hai ya nahi uska resutl show karna:
    1. Student percantage:
        1. 80-100% = 1st div result
        1. 60-79.99 = 2nd div result
        1. 40-59.99 = 3rd div result
        1. <39.99 = Fail
1. Yad rahe ki student rollnumber ki behalf par result show karna hai. aur ek studnet ka result show hone ke bad theek niche option dena hai yes/no (y/n) ka ki agar aap kisi aur student ka result dekhna cahte hain then y enter kare ya nahi dekhna cahte hain to n enter kare.
1. y enter karne par: user se student roll number lena hai then uska result same tarike se show karn hai.

> Note: Har concept me jaha par bhi user se input lena hai aap ko us har ek jagah par validation karna hai ki agar use kuch aur input de raha hai to message show karna.

