define m = Character("[player_name]", color='#004400')
define e = Character("Աղջիկ", color='#440000')
define s = Character("Աղջիկ", color='#440044')
define f = Character("Զինվոր", color='#225522')
define g = Character("Գեներալ", color='#111111')
define gexam = Character("Գեղամ", color='#112211')
define k2 = Character("Կապավոր 2", color='#660055')
define k1 = Character("Կապավոր 1", color='#006655')
define Shahen = Character("Շահեն", color='#006655')

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
image bg antar = "antar.png"


label start:
    scene bg black
    with Dissolve(2.0)
    "Եկեղեցին արդեն հեռվից երևում էր․․․"

    $ player_name = renpy.input("Ձեր անունն է։")

    $ girl_killed = False
    $ girl2_hog_tanel = False

    scene bg mybackground
    with Dissolve(2.0)

    play audio "bell.mp3"
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
            "Լուսածագին գեներալներն ու հրամանատարները ճշտեցին գյուղի դիրքը։"
            scene bg black
            with Dissolve(0.5)
            play audio "car1.mp3"
            "Գիշերվա ընթացքում անընդհատ լսվում էին շարժիչի ձայները․․․"
            play audio "car2.mp3"
            "․․․սակայն մենք հանգիստ էինք, որովհետև դա մեր օգնությունն էր։"

    m "Չորս կողմից տապալված հեռագրասյուների,
էլեկտրասյուների, առաջնորդների մեծադիր յուղանկարների, գալարաթափ
լարերի, մետաղների ու, քթներիս առած ինչևոր բուրմունքների միջով․․․"

    scene bg my5bg
    m "Բամբակի դաշտերով էլ անցանք ու հողի դողը ոտքներիս տակ` մտանք գյուղ:"

    scene bg axjik
    m "Հետո նրանց աղջիկը, որ զինվորական շորերով նստած «Շիլկայի» վրա մեր տանկերն էր ոչնչացնում, նրան յուրայինները լքել էին, հանձնվեց հուսախաբ:"

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



    scene bg hraman
    m "Մեզ գյուղը ցույց տվեցին: Ռադիոկապով հրաման տվողներն ու գեներալներն էլ էլի սկսեցին․․."

    g "Այն գյուղը վերցրեք ու բազա դրեք:"
    scene bg hardzakum
    play audio "rumble.wav"
    "Հողը դողաց մեր ոտքերի տակ..."
    play audio "armored.wav"
    "...մետաղներ, գալարաթափ լարեր, հեռագրասյուներ, էլեկտրասյուներ, առաջնորդների մեծադիր յուղանկարներ:"

    scene bg black
    with Dissolve(1.0)
    show soldier still:
        ypos 0.3
        xalign 1.2
        linear 0.3 xpos 0.8
    g "Ստուգեք տները մեկ առ մեկ, թաքնվածներ մնացած չլինեն:"

    scene bg shun
    play audio "barking.mp3"
    with Dissolve(4.0)
    m "Նրանց շները պատառոտում էին մեզ, ամեն կողպեքը կախած փակ դռան ետեւը նրանք իրենց գամփռներին էին դրել..."
    play audio "krakoc.mp3"
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
            play audio "krakoc.mp3"
            ""
        "Մատնել":
            if girl_killed == True:
                g "Սպանել էտ աղջկան"
                play audio "krakoc.mp3"
            if girl_killed == False:
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
                play audio "radio.mp3"
                show kapavor talk at left:
                    zoom 0.5
                k1 "....կարո՞ղ է տեսել էք Սերոբին։ Ձեր հետ էր․․․"
                play audio "radio.mp3"
                k2 "Անջատիր, ապուշ, կյանքումդ երբեւէ միացե՞լ ես, անհրաժեշտության պահին միշտ էլ փորլուծ ես ունեցել, անջատիր..."
                k2 "Գիշերայինով դուրս գամ, գիշերային գիծը միշտ էլ ազատ են թողնում, յոթանասունինն ազատ կլինի:"

            if girl_killed == True:
                scene bg black
                "Բոլորը թունավորվեցին և մահացան"
                return

        "Սպասել":
            scene bg no_water
            m "Հրամանատարը գնացել էր հավաքի, որպեսզի քննարկեին հարձակման պլանները։"
            m "Ծարավը սաստկանում էր, մենք ջուր էինք ուզում։"

            show soldier still at right
            f "Համբերեք, կարող է թիկունքից ջուր են հասցնում, կապով կպարզենք"
            scene bg kap
            show soldier still at right
            m "Շարժական ռադիոկայանը միացրինք, մեկը դարձյալ Սերոբին էր ուզում:"
            play audio "radio.mp3"
            show kapavor talk at left:
                zoom 0.5
            k1 "....կարո՞ղ է տեսել էք Սերոբին։ Ձեր հետ էր․․․"
            k2 "Անջատիր, ապուշ, կյանքումդ երբեւէ միացե՞լ ես, անհրաժեշտության պահին միշտ էլ փորլուծ ես ունեցել, անջատիր..."
            play audio "radio.mp3"
            k2 "Գիշերայինով դուրս գամ, գիշերային գիծը միշտ էլ ազատ են թողնում, յոթանասունինն ազատ կլինի:"
            m "Հրամանատարը վեջապես վերադարձավ և տեղի տվեց, միայն թե եռացրած ջրի առաջին բաժակն ինքը խմեց։"



    scene bg hardzakum
    m "Մի քանի օր էլ անցավ..."
    scene bg katu_shun
    m "Գյուղի չորս ծագերից դուրս եկան մանր ու խոշոր, գույնզգույն, վիրավոր ու փրկված կատուների խմբեր ու շների ոհմակներ։"
    m "Նրանք հուսահատ գողանում էին մեր հացը․․․"

    m "Այդ կենդանիների սոված ձայներն ու ճիչերը մեզ նյարդայնացնում էին։"

    scene bg parek
    play audio "gisherayin.mp3"
    m "Գիշերը գյուղում պարեկություն անողներիս եւ բազայի շուրջը պահակակետի
       կանգնածներիս համար խախտվում էր բնական լռությունը:"
    m "Միջավայրի աղմուկն ու թշնամու ոտնաձայները շփոթում էինք, չէինք կարողանում
       տարորոշել:"

    scene bg gisher
    play audio "door.mp3"
    m "Գիշերվա հետ հարավից ու հյուսիսից փչող քամին ծեծում, շրխկացնում ու
       ճռռացնում էր հարյուրավոր տների բաց ու փակ դռներն ու լուսամուտները:"
    m "Ինչքան էլ մենք գիտեինք, որ հիմա թիկունքում շրխկալու է դուռն ու
        լուսամուտը, այնուամենայնիվ, վեր էինք թռչում։"
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
    scene bg Shahen
    Shahen "Մեր գիշերատեղի դիմացի տունը պիտի հրկիզենք։ Այդպես էլ դիրքի կանգնել հնարավոր չէ: "
    Shahen "Կտուրը կղմինդրից է,
    հենց դրանք մի թեթեւ տեղաշարժ են կատարում, ոնց որ այնտեղ մարդ ման գա: "
    Shahen "Էդ տունը չպիտի մնա, կմիամտվենք, ու մի օր թշնամին կբարձրանա կտուր"
    g "Չէ, այդպիսի բան անել պետք չէ: Չանեք եւ` վերջ։"
    scene bg post
    m "Ներսումս մեկը կա, ես նրան չեմ տեսել, բայց նրա հետ մի օր կգնամ կիսավեր տաճարը, արյան ավազանի մոտ"
    gexam "Նա քո զոհը կդառնա"
    m "Ոչ, ոչ, նա ոչ մի փորձության չի դիմանա ու ինձ կմատնի"
    gexam "Թուլություն է, երակները լցնելու... թե չէ դեռ չեղածը դու ինչի՞ց ես իմանում, որ պատահելու է..."
    play audio "antar_dzayn.mp3"
    "Հանկարծ անտառում լսում են մի տարօրինակ ձայն՝ գնա՞ն ստուգե՞ն, թե՞ մնան դիրքերում։"
    menu:
        "Ստուգել":
                scene bg antar
                "Զինվորները նկատում են թշնամու հետախույզի։"
                menu:
                    "Կրակել և սպանել"
                        play audio "krakoc.mp3"
                    "Փորձել գերի վերցնել, որպեսզի ինֆորմացիա իմանան։"
                        play audio "krakoc.mp3"
                        play audio "krakoc.mp3"
                    "Հետախույզը արագորեն փոխում է իրավիճակը և սպանում երկուսին էլ։"
                    "Ur dead, game end"
        "Ուշադրություն չդարձնել":
            "d"

    return


label dead_1:
    "ur dead"
    return

    "sdfas dfdf"