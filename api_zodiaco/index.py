import web

render = web.template.render("api_zodiaco/")


class Index():
    def GET(self):
        impresion = None
        return render.index(impresion)

    def POST(self):
        form = web.input()
        mes = int(form['mes'])
        dia = int(form['dia'])
        signo = ("capricornio", "acuario", "piscis", "aries", "tauro",
                 "géminis", "cáncer", "leo", "virgo", "libra", "escorpio",
                 "sagitario")
        fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

        mes -= 1
        if (dia > fechas[mes]):
            mes += 1
        if (mes == 12):
            mes = 0

        buscar = signo[mes]
        impresion = []

        todosLosHoroscopos = {
            "signos": [{
                "signo":
                "Acuario",
                "elemento":
                "Aire",
                "numeroDeLaSuerte":
                "4, 8, 13, 17, 22, 26",
                "color":
                "Azul, Verde-Azul, Gris, Negro",
                "texto":
                "En el trabajo Acuario has puesto toda la carne en el asador y ahora podrás relajarte. En este día recibirás un dinero que no esperabas. Tendrás que administrar mejor tus recursos económicos, así te cundirán más. Si eres valiente con los negocios, te irá muy bien, pero debes arriesgarte. Tu pareja te prepara una sorpresa. Tus seres queridos van a darte una gran alegría este día, te emocionarás. En el amor debes seguir tus propios impulsos y no la opinión de los demás. Vas a llevarte una importante sorpresa en las relaciones, y será bastante positiva. Vas a estar estupendamente en lo personal y en lo sentimental este día. En la salud tu estado de ánimo será un poco negativo, tienes que ver lo bueno de las cosas. Tienes algunas molestias musculares, pero con ejercicio ligero se te pasarán."
            }, {
                "signo":
                "piscis",
                "elemento":
                "Agua",
                "numeroDeLaSuerte":
                "3, 7, 12, 16, 21, 25, 30, 34, 43, 52",
                "color":
                "Mauve, Lila, Púrpura, Violeta, Verde mar",
                "texto":
                "No dudes en pedir ayuda si haces algo por primera vez, así aprenderás bien y lo harás mejor. Tus ahorros aumentarán por un ingreso inesperado, valóralo y guarda un poco. Deberías escuchar los buenos consejos que te dará un familiar sobre el trabajo. Pueden hacerte una oferta bastante interesante, escúchala con atención. Puede que te distancies un poco de alguien a quien quieres, intenta evitarlo. En el amor, si tienes pareja, tendréis una buena conexión entre vosotros, estaréis bien. Vas a estar estupendamente en lo personal y en lo sentimental. Te conviene descargar el exceso de adrenalina, prueba a hacer ejercicio. Tienes la mente despejada para las actividades intelectuales, aprovecha. Te sientes bien y con dinamismo, intenta realizar lo que tienes en mente. Estás bien, no descuides tu salud y mantén ese buen ánimo que tienes, los resultados no se harán esperar. "
            }, {
                "signo":
                "aries",
                "elemento":
                "Fuego",
                "numeroDeLaSuerte":
                "1, 9",
                "color":
                "Rojo",
                "texto":
                "Sufrirás envidias en el entorno laboral Aries, y con razón, actúa con prudencia. Si trabajas por tu cuenta te irán muy bien las relaciones públicas y sociales. Tus iniciativas laborales tendrán su recompensa, no dejes de ofrecerlas. Quieres hacer las cosas a tu manera en el trabajo, pero debes amoldarte un poco. Vas a tener una relación especial con las personas de tu signo o de Escorpio. Tu relación con tu familia será amena y distendida, os llevareis bien. Puede que llegue una nueva ilusión a tu vida que contribuya a animarte. Te sientes bien y tienes ganas de viajar y de moverte, hazlo si te es posible. Si te sigues tomando en serio la alimentación, tendrás buenos resultados. Procura buscar un sitio tranquilo para relajarte, necesitas desconectar. Tienes una actitud muy positiva ante la vida que te beneficiará en todo."
            }, {
                "signo":
                "tauro",
                "elemento":
                "Tierra",
                "numeroDeLaSuerte":
                "2, 4, 6, 11, 20, 29, 37, 47, 56",
                "color":
                "Azul, Rosa, Verde",
                "texto":
                "El trabajo te dará muchas satisfacciones Tauro, céntrate en él este día. Tendrás bastante suerte con el dinero pero aun así no debes arriesgarte mucho. Tendrás iniciativa y la pondrás en práctica con buenos resultados. Hay que tener discreción con tus logros, no es bueno ganarse adversarios, y menos en estos momentos. Tu familia te hará pasar momentos agradables, tu relación será muy buena. Creer que tienes la razón siempre te puede traer problemas, intenta ser flexible. En el amor, vas a lanzarte a una nueva aventura pronto y los resultados serán positivos. Por fin podrás despejarte y relajarte, harás algo que te divierta realmente. Tu salud será inmejorable y tendrás mucha fuerza, no habrá quien te pare. Si te cuesta dormir algo más de lo normal procura cenar un poco menos.  "
            }, {
                "signo":
                "geminis",
                "elemento":
                "Aire",
                "numeroDeLaSuerte":
                "3, 8, 12, 23",
                "color":
                "Verde, Amarillo",
                "texto":
                "Puedes conseguir algún triunfo Géminis, sigue trabajando para continuar en racha. Recibirás propuestas interesantes de todo tipo y tendrás la opción de elegir. Tendrás ideas nuevas e iniciativas para tu trabajo que funcionarán bien. Si estás desempleado, ahora puedes encontrar algo muy bueno, anímate. Las citas y encuentros que tengas serán varias y divertidas, lo pasarás bien. Tendrás noticias sobre algo o alguien que veías bastante lejos últimamente. Si tienes una relación de pareja, notarás una mejora en la marcha de las cosas. Disfrutarás más que nunca del amor gracias a tus ganas de hacer cosas nuevas. En este día se te recomienda descansar bien o hacer algo para reforzarte. Déjate llevar por lo bueno de la vida y vive el presente, deja los agobios. Dar largos paseos sería muy beneficioso para tu salud y te calmaría también.  "
            }, {
                "signo":
                "cancer",
                "elemento":
                "Agua",
                "numeroDeLaSuerte":
                "2, 7, 11, 16, 20, 25",
                "color":
                "Blanco",
                "texto":
                "Tienes algo de tendencia a realizar gastos innecesarios Cáncer, intenta controlarte. Tendrás que resolver problemas que surjan en el trabajo y lo harás muy bien. En lo profesional tendrás que poner más energía, sólo así te irá bien en el futuro. Puede que te paguen o te devuelvan algo que ya casi habías olvidado. Este día va a estar plagado de contactos o comunicaciones, no pararás. Dedica más tiempo a entenderte con los que te rodean, te vendría bien. En el amor, si tienes pareja, debes aclararte con ella, tu actitud es contradictoria. Ante cualquier cosa que surja, actúa con decisión, el resultado será mejor. Trata de comer sano, evita comer fuera de casa los días que te sea posible. Procura hacer ejercicio para descargar adrenalina, te sentará muy bien. Física y mentalmente te sentirás muy bien y además estarás con muy buena salud."
            }, {
                "signo":
                "leo",
                "elemento":
                "Fuego",
                "numeroDeLaSuerte":
                "1, 4, 10, 13, 19, 22",
                "color":
                "Oro, Naranja, Blanco, Rojo",
                "texto":
                "Pronto tendrás que hacer una compra importante Leo, no te excedas con los gastos. Puede haber algún conflicto en tu trabajo, trata de mantenerte al margen. Estás cerca de conseguir tus objetivos en tus tareas, así es que no pares ahora. Serás muy popular en ambientes distintos a los que frecuentas normalmente. Vas a tener mucha facilidad para entablar nuevas relaciones personales. En el amor, si no tienes pareja, alguien puede intentar hacerte compañía, si te interesa. Pero si tienes pareja, habrá una conexión especial entre vosotros, estaréis bien. Durante este día te sentirás con más dinamismo y vitalidad, podrás hacer de todo. El exceso de responsabilidades te está agotando, debes delegar en alguien. Tienes algo de estrés, cuídate, procura dormir más y comer sano. Según pasen los días te irás sintiendo mejor de salud y más fuerte, aumentará tu energía."
            }, {
                "signo":
                "virgo",
                "elemento":
                "Tierra",
                "numeroDeLaSuerte":
                "5, 14, 23, 32, 41, 50",
                "color":
                "Blanco, Amarillo, Beige, Verde Bosque",
                "texto":
                "Tendrás que tomar una decisión importante de trabajo, sigue tu intuición. Te sientes en crisis y cuestionas tu futuro profesional, pero no tienes motivos. Intenta hacer algunos cambios laborales para que vaya como tú quieres. No es el momento de realizar grandes inversiones que te supongan riesgos. Alguien que te quiere te hará un regalo o te sorprenderá con algún detalle de amor. Tu relación de pareja, si la tienes, andará mucho mejor que en días pasados. Un familiar se encuentra con problemas y te sentirás bien al ayudarle. Vas a dedicar más tiempo a tu bienestar físico, y por lo tanto te sentirás bien. Tu tesón y tu perseverancia te ayudarán a lograr tus objetivos, como siempre. Físicamente te encuentras bien y tienes la energía en un punto muy alto. Llevas un ritmo muy fuerte de vida y eso puede pasarte factura, echa el freno.  "
            }, {
                "signo":
                "libra",
                "elemento":
                "Aire",
                "numeroDeLaSuerte":
                "6, 15, 24, 33, 42, 51, 60",
                "color":
                "Azul verde",
                "texto":
                "Tendrás cambios en el trabajo, que sean positivos o no dependerá de tu actitud. Puedes tener muchas ideas nuevas y brillantes en lo laboral, empléalas. Vas a poder hacer alguna que otra compra que habías tenido que postergar. Vas a tener la suerte de tu lado en asuntos de dinero, prueba a invertir. Si no tienes pareja procura salir un poco más y la encontrarás, pon de tu parte. Tienes nuevas expectativas en el amor y eso hará aumentar tu optimismo. No prestes atención a los comentarios de cierto miembro de tu familia. Ten cuidado con tu carácter y no te metas en problemas, lo puedes lamentar. Si quieres mejorar tu imagen mediante un cambio, es el momento oportuno. Te sentirás muy vital y con mucha salud y energía, no dejes que nada lo estropee, pero pon de tu parte."
            }, {
                "signo":
                "escorpio",
                "elemento":
                "Agua",
                "numeroDeLaSuerte":
                "9, 18, 27, 36, 45, 54, 63, 72, 81, 90",
                "color":
                "Escarlata, Rojo",
                "texto":
                "En el trabajo entrarás en una etapa de estabilidad que te sentará bien Escorpio. Te puede surgir un gasto inesperado, pero no te preocupes, ya te repondrás. Estás en un momento muy productivo laboralmente que debes aprovechar. Vas a necesitar mucha mano izquierda con tus jefes, pero tienes recursos. Tendrás muy buenas relaciones este día con los nativos del signo de Virgo. Tendrás que dar apoyo y consejo a un familiar que luego te lo agradecerá. Llevas un ritmo muy alto, a tu pareja y a tus amigos les costará seguirte. Si pidieras consejo a los que te quieren, tus asuntos podrían ir mejor, hazlo. Las discusiones y las tensiones te pueden afectar este día, intenta evitarlas. Alternarás momentos de vitalidad y de desánimo, debes buscar el equilibrio. Deberías mimarte más y prestarle las atenciones necesarias a tu salud."
            }, {
                "signo":
                "sagitario",
                "elemento":
                "Fuego",
                "numeroDeLaSuerte":
                "3, 12, 21, 30",
                "color":
                "Violeta, Púrpura, Rojo, Rosa",
                "texto":
                "Debes actuar con prudencia delante de tus jefes, no es el momento de arriesgar. Puede que tengas que pagar alguna reparación, pero no dejes que te afecte. Procura no discutir en el trabajo, la diplomacia te ayudará mucho más. Te esperan novedades en el terreno laboral y económico, y serán positivas. Relativo al amor, hay una persona que tiene mucho interés en conocerte bien, podrías probar. Vas a hablarle claro a un compañero para ponerle en su sitio, y lo harás bien. Buscarás la armonía que necesitas para aumentar tu bienestar, y lo conseguirás. No repararás en gastos para verte bien, pero lo cierto es que lo conseguirás. Deberías poner un poco de orden en tus horarios y en tu vida en general. No te dejes llevar por tus impulsos y piénsalo bien antes de hacer algo que te afecte a todos los niveles."
            }, {
                "signo":
                "capricornio",
                "elemento":
                "Tierra",
                "numeroDeLaSuerte":
                "1, 4, 8, 10, 13, 17, 19, 22, 26",
                "color":
                "Marrón, Gris, Negro",
                "texto":
                "Debes evitar la rutina en el trabajo Capricornio, tienes que intentar introducir algún tipo de cambio. Tendrás mucha inspiración y progresos profesionales en tus tareas, no dejes de aplicar todas tus ideas. Alguien a quien creías conocer te dará una sorpresa agradable, disfrútalo. Compartirás tus intereses con los que te rodean, habrá una buena conexión. Te enfrentarás a los posibles problemas con temple y serenidad, te irá bien. Disfrutarás más que nunca del amor gracias a tu iniciativa y a tu buen estado de ánimo. Te sobrará energía y entusiasmo en el día a día, todo saldrá como quieres. Si buscas la estabilidad, la vas a encontrar muy pronto, estás en el camino. Estás teniendo mucha tensión, procura cambiar esa actitud que no te conviene. Piensa que estás con mucha energía, encáuzala en todos los campos, verás cómo avanzarás mucho."
            }]
        }

        for sig in todosLosHoroscopos['signos']:
            if buscar == sig['signo']:
                elemento = sig['elemento']
                numeroDeLaSuerte = sig['numeroDeLaSuerte']
                color = sig['color']
                texto = sig['texto']
                dis = {
                    "signo": buscar,
                    "elemento": elemento,
                    "numeroDeLaSuerte": numeroDeLaSuerte,
                    "color": color,
                    "texto": texto
                }
                impresion.append(dis)

        return render.index(impresion)
