define m = Character("[player_name]", color='#004400')
define e = Character("Աղջիկ", color='#440000')
define s = Character("Աղջիկ", color='#440044')
define f = Character("Զինվոր", color='#225522')
define g = Character("Գեներալ", color='#111111')
define gexam = Character("Գեղամ", color='#112211')
define k2 = Character("Կապավոր 2", color='#660055')
define k1 = Character("Կապավոր 1", color='#006655')
define Shahen = Character("Շահեն", color='#006655')
define karo = Character("Կարո", color='#0000aa')

image bg mybackground = "1stbackground.png"
image bg my2bg = "2bg.jpg"
image bg my3bg = "3bg.jpg"
image bg my4bg = "4bg.jpg"
image bg my5bg = "5bg.jpg"
image bg qartez = "qartez.jpg"
image bg ddum = "ddum.jpg"
image bg axjik = "axjik.jpg"
image bg hraman = "hraman.png"
image bg hardzakum = "hardzakum.jpg"
image bg shun = "shun.png"
image bg paharaniAxjik = "paharaniAxjik.jpg"
image bg black = "black.jpg"
image girl handcuffed = "girl.png"
image kapavor talk = "kapavor.png"
image girl2 handcuffed = "girl2.png"
image soldier still = "soldier.png"
image bg hug = "hug.jpg"
image bg no_water = "no_water.jpg"
image bg a_well = "a_well.jpg"
image bg warning = "warning.jpg"
image bg axjkan_jur_berel = "axjkan_jur_berel.jpg"
image bg kap = "kap.jpg"
image bg katu_shun = "katu_shun.jpg"
image bg gisher = "gisher.jpg"
image bg parek = "parek.jpg"
image bg Serob = "Serob.png"
image bg hac_apur = "hac_apur.jpg"
image bg dzi_esh = "dzi_esh.jpg"
image bg lusankarvum = "lusankarvum.jpg"
image bg Shahen = "Shahen.jpg"
image bg post = "post.jpg"
image bg herag = "herag.jpg"
image bg antar = "antar.png"

default girl_killed = False
default girl2_killed = False
default girl2_hog_tanel = False
default girl2_geri = False

label start:
    scene bg black
    with Dissolve(2.0)
    "Եկեղեցին արդեն հեռվից երևում էր․․․"

    $ player_name = renpy.input("Ձեր անունն է։")

    scene bg mybackground
    with Dissolve(2.0)

    play sound "bell.mp3"
    m "Արգելեցին զենքով եկեղեցի մտնել: Մեր հոգու փրկության համար անվճար մոմեր բաժանեցին, եւ մենք, զենքը դռանը թողած, ներսում մոմեր վառեցինք: "
    scene bg my2bg

    play sound "armored.wav"
    m "Հետո սրընթաց արագությամբ վերցնում էինք նրանց գյուղերը:"
    scene bg my3bg

    m "...հեռագրասյուներ․․․առաջնորդների մեծադիր յուղանկարներ․․․գալարաթափ լարեր․․․մետաղներ եւ տարաբնույթ բուրմունքներ արձակող գյուղեր․․․"
    scene bg my4bg

    stop sound fadeout 1.0
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
            "Լուսածագին գեներալներն ու հրամանատարները ճշտեցին գյուղի դիրքը։"
            scene bg black
            with Dissolve(0.5)
            play sound "car1.mp3"
            "Գիշերվա ընթացքում անընդհատ լսվում էին շարժիչի ձայները․․․"
            play sound "car2.mp3"
            "․․․սակայն մենք հանգիստ էինք, որովհետև դա մեր օգնությունն էր։"

    scene bg hardzakum
    m "Չորս կողմից տապալված հեռագրասյուների,
էլեկտրասյուների, առաջնորդների մեծադիր յուղանկարների, գալարաթափ
լարերի, մետաղների ու, քթներիս առած ինչևոր բուրմունքների միջով․․․"

    scene bg my5bg
    m "Բամբակի դաշտերով էլ անցանք ու հողի դողը ոտքներիս տակ` մտանք գյուղ:"

    scene bg axjik
    m "Նրանց աղջիկը, որ զինվորական շորերով նստած «Շիլկայի» վրա մեր տանկերն էր ոչնչացնում, նրան յուրայինները լքել էին, հանձնվեց հուսախաբ:"

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
            play sound "krakoc.mp3"
            scene bg black
            with Dissolve(3.0)
            m "․․․անտանելի ժամանակներ էն․․․"
            $ girl_killed = True

        "Գերի վերցնել":
            m "Մենք նրա շուրջը, ամենքս տարբեր տեղեր էինք նստել։"

            m "Ծոցագրպանից օրագիրը վերցրինք, որտեղ արեւի մասին տողեր կային, շուն
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



    scene bg hraman:
        zoom 1.5
    m "Մեզ գյուղը ցույց տվեցին: Ռադիոկապով հրաման տվողներն ու գեներալներն էլ էլի սկսեցին․․."

    g "Այն գյուղը վերցրեք ու բազա դրեք:"
    scene bg herag
    play sound "rumble.wav"
    "Հողը դողաց մեր ոտքերի տակ..."
    play sound "armored.wav"
    "...մետաղներ, գալարաթափ լարեր, հեռագրասյուներ, էլեկտրասյուներ, առաջնորդների մեծադիր յուղանկարներ:"

    stop sound

    scene bg black
    with Dissolve(1.0)
    show soldier still:
        ypos 0.3
        xalign 1.2
        linear 0.3 xpos 0.8
    g "Ստուգեք տները մեկ առ մեկ, թաքնվածներ մնացած չլինեն:"

    scene bg shun
    play sound "barking.mp3"
    with Dissolve(4.0)
    m "Նրանց շները պատառոտում էին մեզ, ամեն կողպեքը կախած փակ դռան ետեւը նրանք իրենց գամփռներին էին դրել..."
    play sound "krakoc.mp3"
    m "Ներս մտնելուն պես հափռում էին մեր տղաներին, իսկ մենք, ինչքան հասցնում, գնդակահարում էինք նրանց օդի մեջ․․․"

    scene bg paharaniAxjik
    with Dissolve(0.5)
    m "Տներից մեկում մի փոքրիկ աղջիկ տեսանք..."
    m "Հրամանն էր եղել՝ ոչ ոքի ողջ չթողել․․․"



    scene bg black
    with Dissolve(1.0)

    show girl2 handcuffed:
        ypos 0.1
        linear 0.7 xpos 0.3
    m "Էս աղջիկը այնքան վախեցած էր, նույնիսկ չէր կարողանում մի բառ արտասանել․․․"
    s "..."

    menu:
        "Սպանել":
            $ girl2_killed = True
            play sound "krakoc.mp3"
            ""
        "Մատնել":
            if girl_killed == True:
                $ girl2_killed = True
                g "Սպանե՛լ էտ աղջկան։"
                play sound "krakoc.mp3"
            if girl_killed == False:
                $ girl2_geri = True
                scene bg black
                with Dissolve(1.0)

                show girl handcuffed at left
                show girl2 handcuffed at right

                m "Երբ առաջին աղջիկը տեսավ երկրորդին, նրանք վազեցին իրար գրկեցին։"
                m "Նրանց աչքերը լի էին արցունքներով, բայց դրանց խորքում՝ փոքրիկ հույս կար։"
                m "Նրանք գրկում էին միմյանց, ասես մոռացած լինեն ամեն ինչ։"
        "Մոռանալուն տալ":
            show girl2 handcuffed:
                linear 0.7 xpos -0.3
            m "Մի գուցէ գոնե էս մեկին հնարավոր լինի փրկել․․․"
            m "Վերջիվերջո ամեն հրաման պետք չի անհասկացողի պես բառ֊առ֊բառ կատարել։"
        "Ամեն օր հոգ տանել":
            show girl2 handcuffed:
                linear 0.7 xpos 0.1
            m "Մի գուցէ գոնե էս մեկին հնարավոր լինի փրկել։"
            m "Այսինքն հնարավոր լինի գոնե մի քանի օրը մեկ հաց ու ջուր բերել էս տուն․․․"
            $ girl2_hog_tanel = True



    if girl2_hog_tanel == True:
        scene bg axjkan_jur_berel
        "ddd"

    scene bg no_water
    with Dissolve(2.0)
    "Երբ հավաքվեցինք մի տեղ ու բերաններիս մածուկված փոշին էինք թքում, նկատեցինք, որ բոլորիս ջրի տափաշշերն էլ դատարկ են: Գյուղը տակն ու վրա էինք անում, ջուր չկար:"
    scene bg a_well
    gexam "Ջուր... Աստված իմ, ջուր... Մոռացել էի նույնիսկ ինչ համ ունի..."
    scene bg warning
    g "Ոչ ոք չխմի էդ ջրից։ Հնարավոր է, որ թշնամին է թունավորել, որպեսզի հեշտ հաղթանակ տանի։ Համբերեք, կարող է թիկունքից ջուր են հասցնում, կապով կպարզենք:"
    menu:
        "Խմել ջուր":
            if girl_killed == False:
                show girl handcuffed
                s "Ջուրը եռացրեք հետո Խմեք, որպեսզի չթունավորվեք"
                m "Մնում է կապ տանք թիկունք, ասենք որ ջուր ենք գտել։"
                scene bg kap
                show soldier still at right
                m "Շարժական ռադիոկայանը միացրինք, մեկը դարձյալ Սերոբին էր ուզում:"
                play sound "radio.mp3"
                show kapavor talk at left:
                    zoom 0.5
                k1 "....կարո՞ղ է տեսել էք Սերոբին։ Ձեր հետ էր․․․"
                play sound "radio.mp3"
                k2 "Անջատիր, ապուշ, կյանքումդ երբեւէ միացե՞լ ես, անհրաժեշտության պահին միշտ էլ փորլուծ ես ունեցել, անջատիր..."
                k2 "Գիշերայինով դուրս գամ, գիշերային գիծը միշտ էլ ազատ են թողնում, յոթանասունինն ազատ կլինի:"
                k1 ".... ասում են մերսի էտ աղջկա համար․․․"
    
                m "Ի՞նչ նկատի ունի «մերսի» ասելով․․․"

            if girl_killed == True:
                scene bg black
                "Բոլորը թունավորվեցին և մահացան"
                return

        "Սպասել":
            # scene bg no_water
            # m "Հրամանատարը գնացել էր հավաքի, որպեսզի քննարկեին հարձակման պլանները։"
            m "Ծարավը սաստկանում էր, մենք ջուր էինք ուզում։"

            # show soldier still at right
            # f "Համբերեք, կարող է թիկունքից ջուր են հասցնում, կապով կպարզենք"

            scene bg kap
            show soldier still at right
            m "Շարժական ռադիոկայանը միացրինք, մեկը դարձյալ Սերոբին էր ուզում:"
            play sound "radio.mp3"
            show kapavor talk at left:
                zoom 0.5
            k1 "....կարո՞ղ է տեսել էք Սերոբին։ Ձեր հետ էր․․․"
            k2 "Անջատիր, ապուշ, կյանքումդ երբեւէ միացե՞լ ես, անհրաժեշտության պահին միշտ էլ փորլուծ ես ունեցել, անջատիր..."
            play sound "radio.mp3"
            k2 "Գիշերայինով դուրս գամ, գիշերային գիծը միշտ էլ ազատ են թողնում, յոթանասունինն ազատ կլինի:"
            m "Հրամանատարը վեջապես վերադարձավ և տեղի տվեց, միայն թե եռացրած ջրի առաջին բաժակն ինքը խմեց։"



    scene bg hardzakum
    m "Մի քանի օր էլ անցավ..."
    scene bg katu_shun
    m "Գյուղի չորս ծագերից դուրս եկան մանր ու խոշոր, գույնզգույն, վիրավոր ու փրկված կատուների խմբեր ու շների ոհմակներ։"
    m "Նրանք հուսահատ գողանում էին մեր հացը․․․"

    m "Այդ կենդանիների սոված ձայներն ու ճիչերը մեզ նյարդայնացնում էին։"

    scene bg parek
    play sound "gisherayin.mp3"
    m "Գիշերը գյուղում պարեկություն անողներիս եւ բազայի շուրջը պահակակետի
       կանգնածներիս համար խախտվում էր բնական լռությունը:"
    m "Միջավայրի աղմուկն ու թշնամու ոտնաձայները շփոթում էինք, չէինք կարողանում
       տարորոշել:"

    scene bg gisher
    play sound "door.mp3"
    m "Գիշերվա հետ հարավից ու հյուսիսից փչող քամին ծեծում, շրխկացնում ու
       ճռռացնում էր հարյուրավոր տների բաց ու փակ դռներն ու լուսամուտները:"
    m "Ինչքան էլ մենք գիտեինք, որ հիմա թիկունքում շրխկալու է դուռն ու
        լուսամուտը, այնուամենայնիվ, վեր էինք թռչում։"

    stop sound fadeout 2.0
    # axjiknery paxnen stex te che ???

    scene bg Serob
    m "Սերոբին այդպես էլ չգտանք, Սերոբին չե՞ք տեսել, կինն էլ երկու ամսից երեխա է ունենալու: Առաջին անգամն ինձ հետ էր եկել:"

    scene bg hac_apur
    m "Մենք ուզում էինք, որ նա գնա, թողնի ու գնա, ապուր տվեցինք, հացը թաթախելով էր ուտում: "
    f "Դե, ես գնամ, որ տեսնեք, իմաց արեք: "
    scene bg dzi_esh
    m "Իրենց թաքստոցներից գյուղի ամայի փողոցները լցվեցին,սմբակները ջարդոտված ու մազաթափ ավանակներ, ջորիներ, պառաված ձիեր։"
    scene bg lusankarvum
    m "Մենք հեծնում էինք ու նրանց դողդոջուն մեջքների վրա հարմար կեցվածք ընդունած, կրծքներս ուռեցրած` լուսանկարվում:"
    
    if girl2_hog_tanel == True:
        scene bg gisher
        play sound "door.mp3"
        m "Գիշեր էր գալիս, նորից մի փոքր հաց էի տանում էն փոքրիկ աղջկան։"
        m "Ինչքան որ ունեինք, հարյուր անգամ փոքր կտոր էի տանում․․․"
        show girl2 handcuffed at left
        m "Նա արդեն մի քիչ ուշքի էր եկել, հետս ամեն անգամ երկու բառ էր փողանակում"
        s "․․․"
        s "... քույրս ու՞ր է, ուզում եմ գտնել նրան․․․ "
        if girl_killed == True:
            m "Հետաքրիր է, մի քանի շաբաթ առաջ էն աղջկան էինք սպանել։"
            m "Մի գուցե․․․"
        else:
            m "Հետաքրիր է, մի քանի շաբաթ առաջ էն աղջկան էինք գերի վերցրել"
            m "Մի գուցե․․․"
            
        scene bg black
        with Dissolve(1.0)
        m "․․․շատ անտանելի ժամանակներ էն․․․"


    scene bg Shahen
    Shahen "Մեր գիշերատեղի դիմացի տունը պիտի հրկիզենք։ Այդպես էլ դիրքի կանգնել հնարավոր չէ: "
    Shahen "Կտուրը կղմինդրից է,
    հենց դրանք մի թեթեւ տեղաշարժ են կատարում, ոնց որ այնտեղ մարդ ման գա: "
    Shahen "Էդ տունը չպիտի մնա, կմիամտվենք, ու մի օր թշնամին կբարձրանա կտուր"
    g "Չէ, այդպիսի բան անել պետք չէ: Չանեք եւ` վերջ։"
    Shahen "Պետք չէ, բայց այդպես էլ դիրքի կանգնել հնարավոր չէ:"
    Shahen "Ամբողջ գիշերը կտուրից ձեներ էն գալիս, ուղիղ մեր բազայի դիմացն է. էդ
տունը չպիտի մնա, կմիամտվենք, ու մի օր թշնամին կբարձրանա կտուր:"

    scene bg post
    with Dissolve(1.5)
    m "Ես ու Կարոն միասին էինք դիրքի կանգնում ու կանանց կարոտի մասին էինք խոսում:"
    m "Ասում եմ նրան, որ ներսումս մեկը կա, ես նրան չեմ տեսել, բայց նրա հետ մի օր կգնամ կիսավեր տաճարը, արյան ավազանի մոտ"
    karo "Նա քո զոհը կդառնա։"
    m "Ոչ, ոչ, նա ոչ մի փորձության չի դիմանա ու ինձ կմատնի։"
    karo "Թուլություն է, երակները լցնելու... թե չէ դեռ չեղածը դու ինչի՞ց ես իմանում, որ պատահելու է..."
    
    m "Ոչ, ոչ, նա ոչ մի փորձության չի դիմանա ու ինձ կմատնի։"
    play sound "antar_dzayn.mp3"
    m "..."
    m "Հեռու մի տեղից ձայներ էին լսվում..."
    m "Ասացի նրան, որ թիկունքից մեկ֊մեկ ձայներ եմ լսում․․․"
    
    if girl2_killed == False and girl2_geri == False:
        karo "Էհ, երանի ուշադրությանդ․․․"
        karo "Էն օրը այդպես ձայներ լսեցինց, գնացինք տեսանք փոքր աղջիկ էր տներից մեկում․․․"
        karo "Դե հրամանն էր մարդ ողջ չթողել․․․"
        
        stop sound fadeout 1.0
        scene bg black
        with Dissolve(1.0)
        m "․․․չափազանց անտանելի ժամանակներ էն․․․"  
        
        scene bg antar
        with Dissolve(1.0)
        karo "Էդ ձեները ոնց որ անտառի կողմից էին գալիս․․․"
    else:
        karo "Ոնց որ անտառի կողմից էին գալիս․․․"

    menu:
        "Ստուգել":
            jump fight
        "Ուշադրություն չդարձնել":
            karo "Դա լարվածությունից է, էն մեծ գյուղը, որ մտանք, այնտեղ
                    մտնողը ինչ ձայն ասես, որ չէր լսի:"
            karo "Տագնապի պահին ուղեղը սիրում է բաներ հորինել..."

            jump tun_varel

    return

label fight: 
    scene bg antar
    "Զինվորները նկատում են թշնամու հետախույզի։"
    menu:
        "Կրակել և սպանել":
            play audio "krakoc.mp3"
        "Փորձել գերի վերցնել, որպեսզի ինֆորմացիա իմանան։":
            play audio "krakoc.mp3"
            play audio "krakoc.mp3"
            "Հետախույզը արագորեն փոխում է իրավիճակը և սպանում երկուսին էլ։"
            "Ur dead, game end"
    return;
label tun_varel:
    return

label dead_1:
    "ur dead"
    return

    "sdfas dfdf"