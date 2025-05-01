

define m = Character("[player_name]", color='#004400')
define e = Character("Աղջիկ", color='#440000')
define f = Character("Զինվոր", color='#225522')

image bg mybackground = "1stbackground.png"
image bg my2bg = "2bg.jpg"
image bg my3bg = "3bg.jpg"
image bg my4bg = "4bg.jpg"
image bg my5bg = "5bg.jpg"
image bg qartez = "qartez.jpg"
image bg ddum = "ddum.jpg"
image bg axjik = "axjik.jpg"
image bg hraman = "hraman.jpg"
image bg hardzakum = "hardzakum.jpg"
image bg shun = "shun.png"
image bg paharaniAxjik = "paharaniAxjik.jpg"
image bg black = "black.jpg"
image girl handcuffed = "girl.png"
image soldier still = "soldier.png"

label start:

    $ player_name = renpy.input("Ձեր անունն է։")
    scene bg mybackground
    with Dissolve(5.0)

    m "Արգելեցին զենքով եկեղեցի մտնել: Մեր հոգու փրկության համար անվճար մոմեր բաժանեցին, եւ մենք, զենքը դռանը թողած, ներսում մոմեր վառեցինք: "
    scene bg my2bg

    play audio "armored.wav"
    m "Հետո սրընթաց արագությամբ վերցնում էինք նրանց գյուղերը:"
    scene bg my3bg

    m "...հեռագրասյուներ․․․առաջնորդների մեծադիր յուղանկարներ․․․գալարաթափ լարեր․․․մետաղներ եւ տարաբնույթ բուրմունքներ արձակող գյուղեր․․․"
    scene bg my4bg

    m "Քնում էինք քնապարկերի մեջ` թացին, չորին, ցրտին ու տաքին:"

    scene bg my5bg
    m "Դեմ-դիմացի գյուղը վերցնելը դժվար չէր, բայց չէինք ցանկանում տղաներին կորցնել:"

    m "Բայց այսքան հաջողություններից հետո արժե՞ արդյոք չշարունակել առաջ գնալ․․․"
    menu:
        "Ի՞նչ անենք։"

        "Առաջ դեպի հաղթանակ":
            jump dead_1

        "Չարժե ռիսկի դիմել․․․":
            scene bg ddum
            "Դադար առանք ու քնեցինք դեղին դդումների դաշտում։"
            scene bg qartez
            "գեներալներն ու հրամանատարները ճշտեցին գյուղի դիրքը։"
            #????
            "Գիշերվա ընթացքում անընդհատ լսվում էին շարժիչի ձայները․․․"
            "․․․սակայն մենք հանգիստ էինք, որովհետև դա մեր օգնությունն էր։"
    
    scene bg axjik
    "Հետո նրանց աղջիկը, որ զինվորական շորերով նստած «Շիլկայի» վրա մեր տանկերն էր ոչնչացնում, նրան յուրայինները լքել էին, հանձնվեց հուսախաբ:"

    scene bg black 
    with Dissolve(1.5)
    show girl handcuffed
    e "Միայն թե ներարկեք նոր... ես չեմ վախենում:"
    transform left_to_right:
        xalign 0.
        linear 2 xalign 1.
        repeat
    menu:   

        "Սպանել":
            play audio "krakoc.mp3"
            scene bg black
            with Dissolve(3.0)
            "․․․անտանելի ժամանակներ էն․․․"
        "Գերի վերցնել":
            "Մենք նրա շուրջը, ամենքս տարբեր տեղեր էինք նստել։"

            "Ծոցագրպանից օրագիրը վերցրինք, որտեղ արեւի մասին տողեր կային, շուն
                գեներալների, հաց չմատակարարող պահեստապետերի ու իր գործիքով մեր
                խփած տանկերի քանակի մասին:"
            
            show girl handcuffed:
                linear 0.7 xpos 0.3
            show soldier still:
                xalign 1.2
                ypos 0.3
                linear 0.7 xpos 0.8
            f "Լավ էլ ուրախանում եք, նստել ինչի՞ն եք սպասում։"
            show girl handcuffed:
                linear 0.3 zoom 0.7
            show soldier still:
                linear 0.3 zoom 1.2

            f "Տարեք, միաժամանակ երեք անցքն էլ փակեք, մի դրա
երակներին նայեք, տարեք այդ գործն արեք, դրա նմաններն այդպիսի բաներ
շատ են սիրում:"



    scene bg hraman
    "Այն գյուղը վերցրեք ու բազա դրեք:"
    scene bg hardzakum
    play audio "rumble.wav"
    "Հողը դողաց մեր ոտքերի տակ..."
    play audio "armored.wav"
    "...մետաղներ, գալարաթափ լարեր, հեռագրասյուներ, էլեկտրասյուներ, առաջնորդների մեծադիր յուղանկարներ:"
    scene bg shun
    "sdf"
    play audio "krakoc.mp3"
    scene bg paharaniAxjik
    menu:
        "Սպանել":
            "sdf"
        "Մատնել":
            "sdf"
        "Մոռանալուն տալ":
            "sdf"
        "Ամեն օր հոգ տանել":
            "sdf"


    return

label dead_1:
    "ur dead"
    return

    "sdfas dfdf"