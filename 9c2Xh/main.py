import pygame
import random

RES = (1280, 820)

pygame.init()

pygame.display.set_icon(pygame.image.load('sprite/ui/cube/gameP.bmp'))
sc = pygame.display.set_mode((RES[0], RES[1]))
pygame.display.set_caption("9c2Xh")

clock = pygame.time.Clock()

curent_scene = None
def switch_scene(scene):
    global curent_scene
    curent_scene = scene

def finalDialog():
    running = True
    FPS = 60

    FontTXTD = pygame.font.Font('Font/2.ttf', 30)
    TxtD = FontTXTD.render('hey we fucked him up', False, (0, 255, 0))
    TXTrect = TxtD.get_rect(center=(RES[0]//2-460, RES[1]//2+380))

    select = 0

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            if e.type == pygame.KEYDOWN:
                select += 1
        sc.fill((255, 255, 255))
        if select == 0:
            TxtD = FontTXTD.render('hey we fucked him up', False, (0, 255, 0))
        if select == 1:
            TxtD = FontTXTD.render('cool', False, (139, 0, 235))
        if select == 2:
            TxtD = FontTXTD.render('Well, from now on you are my angels who will protect these sinful lands', False, (139, 0, 235))
        if select == 3:
            TxtD = FontTXTD.render('That is, we killed some kind of tarantula and you make us angels?', False, (0, 255, 0))
        if select == 4:
            TxtD = FontTXTD.render('...', False, (139, 0, 235))
        if select >= 5:
            running = False
            switch_scene(mainMenu)
        sc.blit(TxtD, TXTrect)
        pygame.display.update()
        clock.tick(FPS)

def dieScene():
    running = True
    FPS = 60

    fontText = pygame.font.Font('Font/4.ttf', 25)
    Text = fontText.render('Well....', False, (139, 0, 235))
    TextRect = Text.get_rect(center=(100, 750))

    isKey = False

    Frame = 0

    select = 0

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            if e.type == pygame.KEYDOWN:
                if isKey:
                    select += 1
        sc.fill((0, 0, 0))
        if select == 0:
            Text = fontText.render('Well....', False, (139, 0, 235))
        if select == 1:
            Text = fontText.render('Try Again', False, (139, 0, 235))
        if select == 2:
            running = False
            switch_scene(mainMenu)
        if Frame <= 50:
            Frame += 1
        if Frame > 50:
            isKey = True
            sc.blit(Text, TextRect)
        pygame.display.update()
        clock.tick(FPS)

level = 1
def sceneGame():
    global level

    NumberSelect = pygame.mixer.Sound('Audio/SFX/selectNumber.wav')
    ShieldSelect = pygame.mixer.Sound('Audio/SFX/selectShield.wav')
    skipSelect = pygame.mixer.Sound('Audio/SFX/skip.wav')
    confSelect = pygame.mixer.Sound('Audio/SFX/conf.wav')
    startSelect = pygame.mixer.Sound('Audio/SFX/playerHit.wav')

    IoannUI = pygame.image.load('sprite/ui/character/Ioann/1.png').convert_alpha()
    IoannUI = pygame.transform.scale(IoannUI, (350, 132))
    IoannRect = IoannUI.get_rect(center=(195, 250))

    AnnaUI = pygame.image.load('sprite/ui/character/Anna/1.png').convert_alpha()
    AnnaUI = pygame.transform.scale(AnnaUI, (350, 132))
    AnnaRect = AnnaUI.get_rect(center=(195, 100))

    ValeriaUI = pygame.image.load('sprite/ui/character/Valeria/1.png').convert_alpha()
    ValeriaUI = pygame.transform.scale(ValeriaUI, (350, 132))
    ValeriaRect = ValeriaUI.get_rect(center=(195, 405))


    backImage = pygame.image.load('sprite/ui/back.png').convert_alpha()
    backImage  = pygame.transform.scale(backImage, (RES[0], RES[1]+150))
    backImage.set_alpha(170)
    backRect = backImage.get_rect(center=(RES[0]//2, RES[1]//2))


    numberCube = pygame.image.load('sprite/ui/cube/number.png').convert_alpha()
    numberCube = pygame.transform.scale(numberCube, (360, 355))
    numberCube.set_alpha(150)
    numberRect = numberCube.get_rect(center=(470, 649))

    shieldCube = pygame.image.load('sprite/ui/cube/shield.png').convert_alpha()
    shieldCube = pygame.transform.scale(shieldCube, (364, 364))
    shieldCube.set_alpha(150)
    shieldRect = shieldCube.get_rect(center=(650, 659))

    CancleCube = pygame.image.load('sprite/ui/cube/Cancle.png').convert_alpha()
    CancleCube = pygame.transform.scale(CancleCube, (360, 355))
    CancleCube.set_alpha(150)
    CancleRect = CancleCube.get_rect(center=(820, 649))

    arowImage = pygame.image.load('sprite/ui/select.png').convert_alpha()
    arowImage = pygame.transform.scale(arowImage, (42, 42))
    arowRect = arowImage.get_rect(center=(395, 100))

    StartImage = pygame.image.load('sprite/ui/start.png').convert_alpha()
    StartImage = pygame.transform.scale(StartImage, (320, 320))
    StartRect = StartImage.get_rect(center=(1085, 665))

    isDamage = True
    isStart = False

    enemyBandit = pygame.image.load('sprite/enemy/bandit/1.png').convert_alpha()
    enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
    banditRect = enemyBandit.get_rect(center=(1080, RES[1]//2-170))

    if level == 1 or level == 4:
        enemyBandit = pygame.image.load('sprite/enemy/bandit/1.png').convert_alpha()
        enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
        banditRect = enemyBandit.get_rect(center=(1080, RES[1]//2-170))
    if level == 2 or level == 6:
        enemyBandit = pygame.image.load('sprite/enemy/ban/1.png').convert_alpha()
        enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
        banditRect = enemyBandit.get_rect(center=(1080, RES[1]//2-170))
    if level == 3 or level == 8:
        enemyBandit = pygame.image.load('sprite/enemy/blob/1.png').convert_alpha()
        enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
        banditRect = enemyBandit.get_rect(center=(1080, RES[1]//2-170))
    if level == 5 or level == 7:
        enemyBandit = pygame.image.load('sprite/enemy/gasman/1.png').convert_alpha()
        enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
        banditRect = enemyBandit.get_rect(center=(1080, RES[1]//2-170))
    if level == 9:
        enemyBandit = pygame.image.load('sprite/enemy/Tarantule/1.png').convert_alpha()
        enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
        banditRect = enemyBandit.get_rect(center=(1080, RES[1]//2-170))


    shieldIcon = pygame.image.load('sprite/ui/shieldIcon.png').convert_alpha()
    shieldIcon = pygame.transform.scale(shieldIcon, (64, 64))
    shieldIRect = shieldIcon.get_rect(center=(300, 105))

    enemyNumber = random.randint(5, 25)

    numberAnna = 1
    numberIoann = 1
    numberValeria = 1

    fontNumber = pygame.font.Font('Font/3.ttf', 30)

    enemyStroke = None

    if level == 1 or level == 4:
        enemyStroke = 3
    if level == 2 or level == 6:
        enemyStroke = 6
    if level == 3 or level == 8:
        enemyStroke = 4
    if level == 5 or level == 7:
        enemyStroke = 5
    if level == 9:
        enemyStroke = 11

    characterAttack = 1

    selectCube = 0
    selectCharacter = 1

    isKey = False

    timeDamge = 0

    FrameEnemyNumber = 0
    isAnimTXT = True

    isCancleAnna = False
    isCancleIoann = False
    isCancleValeria = False

    AnnaStronk = 5
    IoannStronk = 3
    ValeriaStonk = 5

    isShieldAnna = False

    isShieldIoann = False

    isShieldValeria = False

    FrameArow = 0

    KeyZ = pygame.image.load('sprite/ui/keyboard/Z.png').convert_alpha()
    KeyZ = pygame.transform.scale(KeyZ, (42, 42))
    KeyZ.set_alpha(90)
    KeyZRect = KeyZ.get_rect(center=(1095, 585))

    KeyF = pygame.image.load('sprite/ui/keyboard/F.png').convert_alpha()
    KeyF = pygame.transform.scale(KeyF, (32, 32))
    KeyF.set_alpha(90)
    KeyFRect = KeyF.get_rect(center=(483, 540))

    KeyB = pygame.image.load('sprite/ui/keyboard/B.png').convert_alpha()
    KeyB = pygame.transform.scale(KeyB, (35, 35))
    KeyB.set_alpha(90)
    KeyBRect = KeyB.get_rect(center=(643, 541))

    KeyJ = pygame.image.load('sprite/ui/keyboard/J.png').convert_alpha()
    KeyJ = pygame.transform.scale(KeyJ, (32, 32))
    KeyJ.set_alpha(90)
    KeyJRect = KeyJ.get_rect(center=(810, 540))

    fontTXT = pygame.font.Font('Font/4.ttf', 20)
    ConfirmTXT = fontTXT.render('Confirm selection', False, (255, 255, 255))
    ConfirmTXT.set_alpha(50)
    ConfirmTXTRect = ConfirmTXT.get_rect(center=(RES[0]//2, 490))

    KeyI = pygame.image.load('sprite/ui/keyboard/I.png').convert_alpha()
    KeyI = pygame.transform.scale(KeyI, (32, 32))
    KeyI.set_alpha(90)
    KeyIRect = KeyI.get_rect(center=(RES[0]//2, 450))

    cancleIcon = pygame.image.load('sprite/ui/cancle.png').convert_alpha()
    cancleIcon = pygame.transform.scale(cancleIcon, (64, 64))
    cancleIRect = cancleIcon.get_rect(center=(300, 105))

    swordIcon = pygame.image.load('sprite/ui/sword.png').convert_alpha()
    swordIcon = pygame.transform.scale(swordIcon, (42, 42))
    swordRect = swordIcon.get_rect(center=(210, 65))

    Frame1 = pygame.image.load('sprite/ui/Frame1.png').convert_alpha()
    Frame1 = pygame.transform.scale(Frame1, (587, 499))
    Frame1.set_alpha(150)
    Frame1Rect = Frame1.get_rect(center=(650, 659))

    FrameDieEnemy = 0
    XPosEnemy = 1080

    shield = 5

    fontShield = pygame.font.Font('Font/1.ttf', 19)
    shieldTXT = fontShield.render(str(shield), False, (255, 255, 255))
    shieldTXT.set_alpha(120)
    shieldTRect = shieldTXT.get_rect(center=(675, 657))

    isAnimStart = False
    startAnim = 0

    running = True
    FPS = 60
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                switch_scene(None)
                running = False
            if e.type == pygame.KEYDOWN:
                if isKey:
                    if e.key == pygame.K_f:
                        NumberSelect.play()
                        ConfirmTXT.set_alpha(250)
                        numberCube.set_alpha(250)
                        shieldCube.set_alpha(150)
                        CancleCube.set_alpha(150)
                        shieldRect = shieldCube.get_rect(center=(650, 659))
                        numberRect = numberCube.get_rect(center=(470, 625))
                        CancleRect = CancleCube.get_rect(center=(820, 649))
                        selectCube = 1
                    if e.key == pygame.K_b:
                        ShieldSelect.play()
                        ConfirmTXT.set_alpha(250)
                        shieldCube.set_alpha(250)
                        CancleCube.set_alpha(150)
                        numberCube.set_alpha(150)
                        shieldRect = shieldCube.get_rect(center=(650, 630))
                        numberRect = numberCube.get_rect(center=(470, 649))
                        CancleRect = CancleCube.get_rect(center=(820, 649))
                        selectCube = 2
                    if e.key == pygame.K_j:
                        skipSelect.play()
                        ConfirmTXT.set_alpha(250)
                        shieldCube.set_alpha(150)
                        CancleCube.set_alpha(250)
                        numberCube.set_alpha(150)
                        shieldRect = shieldCube.get_rect(center=(650, 659))
                        numberRect = numberCube.get_rect(center=(470, 649))
                        CancleRect = CancleCube.get_rect(center=(820, 625))
                        selectCube = 3
                    if e.key == pygame.K_i:
                        if selectCube == 1 and selectCharacter <= 3:
                            confSelect.play()
                            if selectCharacter == 1 and AnnaStronk > 0:
                                numberAnna = random.randint(15, 55)
                            if selectCharacter == 2 and IoannStronk > 0:
                                numberIoann = random.randint(10, 50)
                            if selectCharacter == 3 and ValeriaStonk > 0:
                                numberValeria = random.randint(11, 65)
                            selectCharacter += 1
                        if selectCube == 2 and selectCharacter <= 3 and shield > 0:
                            confSelect.play()
                            if selectCharacter == 1:
                                shield -= 1
                                isShieldAnna = True
                            if selectCharacter == 2:
                                shield -= 1
                                isShieldIoann = True
                            if selectCharacter == 3:
                                shield -= 1
                                isShieldValeria = True
                            selectCharacter += 1
                        if selectCube == 3 and selectCharacter <= 3:
                            confSelect.play()
                            if selectCharacter == 1:
                                isCancleAnna = True
                            if selectCharacter == 2:
                                isCancleIoann = True
                            if selectCharacter == 3:
                                isCancleValeria = True
                            selectCharacter += 1
                    if e.key == pygame.K_z:
                        isAnimStart = True
                        startSelect.play()
                        ConfirmTXT.set_alpha(50)
                        isStart = True
                        isKey = False

        if AnnaStronk <= 0 and IoannStronk <= 0 and ValeriaStonk <= 0:
            running = False
            switch_scene(dieScene)

        if isAnimStart:
            if startAnim == 11:
                isAnimStart = False
                startAnim = 0
                StartRect = StartImage.get_rect(center=(1085, 665))
            if startAnim == 6:
                StartRect = StartImage.get_rect(center=(1085, 685))
            startAnim += 1
        shieldTXT = fontShield.render(str(shield), False, (255, 255, 255))
        if selectCube == 0:
            ConfirmTXT.set_alpha(150)
            numberCube.set_alpha(150)
            shieldCube.set_alpha(150)
            CancleCube.set_alpha(150)
            shieldRect = shieldCube.get_rect(center=(650, 659))
            numberRect = numberCube.get_rect(center=(470, 649))
            CancleRect = CancleCube.get_rect(center=(820, 649))
        if level == 1 or level == 4:
            if enemyStroke == 3:
                enemyBandit = pygame.image.load('sprite/enemy/bandit/1.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 2:
                enemyBandit = pygame.image.load('sprite/enemy/bandit/2.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 1:
                enemyBandit = pygame.image.load('sprite/enemy/bandit/3.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 0:
                isKey = False
                enemyBandit = pygame.image.load('sprite/enemy/bandit/5.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
                if FrameDieEnemy == 150:
                    running = False
                    switch_scene(nextLevel)
                if FrameDieEnemy > 20:
                    XPosEnemy += 6
                    banditRect = enemyBandit.get_rect(center=(XPosEnemy, RES[1]//2-170))
                FrameDieEnemy += 1
        if level == 2 or level == 6:
            if enemyStroke == 6:
                enemyBandit = pygame.image.load('sprite/enemy/ban/1.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 5:
                enemyBandit = pygame.image.load('sprite/enemy/ban/2.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 4:
                enemyBandit = pygame.image.load('sprite/enemy/ban/3.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 3:
                enemyBandit = pygame.image.load('sprite/enemy/ban/4.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 2:
                enemyBandit = pygame.image.load('sprite/enemy/ban/5.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 1:
                enemyBandit = pygame.image.load('sprite/enemy/ban/6.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 0:
                enemyBandit = pygame.image.load('sprite/enemy/ban/7.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
                if FrameDieEnemy == 150:
                    running = False
                    switch_scene(nextLevel)
                if FrameDieEnemy > 20:
                    XPosEnemy += 6
                    banditRect = enemyBandit.get_rect(center=(XPosEnemy, RES[1]//2-170))
                FrameDieEnemy += 1
        if level == 3 or level == 8:
            if enemyStroke == 4:
                enemyBandit = pygame.image.load('sprite/enemy/blob/1.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (314, 314))
            if enemyStroke == 3:
                enemyBandit = pygame.image.load('sprite/enemy/blob/2.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (314, 314))
            if enemyStroke == 2:
                enemyBandit = pygame.image.load('sprite/enemy/blob/3.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (314, 314))
            if enemyStroke == 1:
                enemyBandit = pygame.image.load('sprite/enemy/blob/4.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (314, 314))
            if enemyStroke == 0:
                enemyBandit = pygame.image.load('sprite/enemy/blob/5.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (314, 314))
                if FrameDieEnemy == 150:
                    running = False
                    switch_scene(nextLevel)
                if FrameDieEnemy > 20:
                    XPosEnemy += 6
                    banditRect = enemyBandit.get_rect(center=(XPosEnemy, RES[1]//2-170))
                FrameDieEnemy += 1
        if level == 5 or level == 7:
            if enemyStroke == 5:
                enemyBandit = pygame.image.load('sprite/enemy/gasman/1.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 4:
                enemyBandit = pygame.image.load('sprite/enemy/gasman/2.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 3:
                enemyBandit = pygame.image.load('sprite/enemy/gasman/3.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 2:
                enemyBandit = pygame.image.load('sprite/enemy/gasman/4.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 1:
                enemyBandit = pygame.image.load('sprite/enemy/gasman/5.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 0:
                enemyBandit = pygame.image.load('sprite/enemy/gasman/6.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
                if FrameDieEnemy == 150:
                    running = False
                    switch_scene(nextLevel)
                if FrameDieEnemy > 20:
                    XPosEnemy += 6
                    banditRect = enemyBandit.get_rect(center=(XPosEnemy, RES[1]//2-170))
                FrameDieEnemy += 1
        if level == 9:
            if enemyStroke == 11:
                enemyBandit = pygame.image.load('sprite/enemy/Tarantule/1.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 10:
                enemyBandit = pygame.image.load('sprite/enemy/Tarantule/2.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 9:
                enemyBandit = pygame.image.load('sprite/enemy/Tarantule/3.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 8:
                enemyBandit = pygame.image.load('sprite/enemy/Tarantule/4.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 7:
                enemyBandit = pygame.image.load('sprite/enemy/Tarantule/5.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 6:
                enemyBandit = pygame.image.load('sprite/enemy/Tarantule/6.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 5:
                enemyBandit = pygame.image.load('sprite/enemy/Tarantule/7.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 4:
                enemyBandit = pygame.image.load('sprite/enemy/Tarantule/8.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 3:
                enemyBandit = pygame.image.load('sprite/enemy/Tarantule/9.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 2:
                enemyBandit = pygame.image.load('sprite/enemy/Tarantule/10.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 1:
                enemyBandit = pygame.image.load('sprite/enemy/Tarantule/11.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
            if enemyStroke == 0:
                enemyBandit = pygame.image.load('sprite/enemy/Tarantule/11.png').convert_alpha()
                enemyBandit = pygame.transform.scale(enemyBandit, (312, 312))
                running = False
                switch_scene(finalDialog)


        if AnnaStronk == 5:
            AnnaUI = pygame.image.load('sprite/ui/character/Anna/1.png').convert_alpha()
            AnnaUI = pygame.transform.scale(AnnaUI, (350, 132))
        if AnnaStronk == 4:
            AnnaUI = pygame.image.load('sprite/ui/character/Anna/2.png').convert_alpha()
            AnnaUI = pygame.transform.scale(AnnaUI, (350, 132))
        if AnnaStronk == 3:
            AnnaUI = pygame.image.load('sprite/ui/character/Anna/3.png').convert_alpha()
            AnnaUI = pygame.transform.scale(AnnaUI, (350, 132))
        if AnnaStronk == 2:
            AnnaUI = pygame.image.load('sprite/ui/character/Anna/4.png').convert_alpha()
            AnnaUI = pygame.transform.scale(AnnaUI, (350, 132))
        if AnnaStronk == 1:
            AnnaUI = pygame.image.load('sprite/ui/character/Anna/5.png').convert_alpha()
            AnnaUI = pygame.transform.scale(AnnaUI, (350, 132))
        if AnnaStronk == 0:
            AnnaUI = pygame.image.load('sprite/ui/character/Anna/6.png').convert_alpha()
            AnnaUI = pygame.transform.scale(AnnaUI, (350, 132))


        if IoannStronk == 3:
            IoannUI = pygame.image.load('sprite/ui/character/Ioann/1.png').convert_alpha()
            IoannUI = pygame.transform.scale(IoannUI, (350, 132))
        if IoannStronk == 2:
            IoannUI = pygame.image.load('sprite/ui/character/Ioann/2.png').convert_alpha()
            IoannUI = pygame.transform.scale(IoannUI, (350, 132))
        if IoannStronk == 1:
            IoannUI = pygame.image.load('sprite/ui/character/Ioann/3.png').convert_alpha()
            IoannUI = pygame.transform.scale(IoannUI, (350, 132))
        if IoannStronk == 0:
            IoannUI = pygame.image.load('sprite/ui/character/Ioann/4.png').convert_alpha()
            IoannUI = pygame.transform.scale(IoannUI, (350, 132))

        if ValeriaStonk == 5:
            ValeriaUI = pygame.image.load('sprite/ui/character/Valeria/1.png').convert_alpha()
            ValeriaUI = pygame.transform.scale(ValeriaUI, (350, 132))
        if ValeriaStonk == 4:
            ValeriaUI = pygame.image.load('sprite/ui/character/Valeria/2.png').convert_alpha()
            ValeriaUI = pygame.transform.scale(ValeriaUI, (350, 132))
        if ValeriaStonk == 3:
            ValeriaUI = pygame.image.load('sprite/ui/character/Valeria/3.png').convert_alpha()
            ValeriaUI = pygame.transform.scale(ValeriaUI, (350, 132))
        if ValeriaStonk == 2:
            ValeriaUI = pygame.image.load('sprite/ui/character/Valeria/4.png').convert_alpha()
            ValeriaUI = pygame.transform.scale(ValeriaUI, (350, 132))
        if ValeriaStonk == 1:
            ValeriaUI = pygame.image.load('sprite/ui/character/Valeria/5.png').convert_alpha()
            ValeriaUI = pygame.transform.scale(ValeriaUI, (350, 132))
        if ValeriaStonk == 0:
            ValeriaUI = pygame.image.load('sprite/ui/character/Valeria/6.png').convert_alpha()
            ValeriaUI = pygame.transform.scale(ValeriaUI, (350, 132))

        numberAnnaText = fontNumber.render(str(numberAnna), False, (255, 255, 255))
        numberARect = numberAnnaText.get_rect(center=(300, 105))

        numberIoannText = fontNumber.render(str(numberIoann), False, (255, 255, 255))
        numberIRect = numberIoannText.get_rect(center=(300, 255))

        numberValeriaText = fontNumber.render(str(numberValeria), False, (255, 255, 255))
        numberVRect = numberValeriaText.get_rect(center=(300, 405))

        ememyNumberTXT = fontNumber.render(str(enemyNumber), False, (255, 255, 255))
        enemyNumberRect = ememyNumberTXT.get_rect(center=(975, RES[1]//2-170))

        if isAnimTXT:
            if FrameEnemyNumber > 20:
                ememyNumberTXT.set_alpha(300)
                FrameEnemyNumber = 0
                isKey = True
                isAnimTXT = False
            randomNumber = random.randint(1, 30)
            ememyNumberTXT = fontNumber.render(str(randomNumber), False, (255, 255, 255))
            ememyNumberTXT.set_alpha(45)
            FrameEnemyNumber += 1

        if FrameArow == 35:
            FrameArow = 0
            arowRect.x = 375
        if FrameArow == 15:
            arowRect.x = 395
        FrameArow += 1

        if isStart:
            if isDamage:
                if characterAttack == 1:
                    if not isShieldAnna:
                        if numberAnna > 0:
                            if numberAnna <= enemyNumber:
                                AnnaStronk -= 1
                            numberAnna -= enemyNumber
                        else:
                            numberAnna = 0
                        if enemyNumber > 0:
                            enemyNumber -= numberAnna
                            if enemyNumber <= numberAnna:
                                enemyStroke -= 1
                        isDamage = False
                    isCancleAnna = False
                    characterAttack = 4
                elif characterAttack == 2:
                    if not isShieldIoann:
                        if numberIoann > 0:
                            if numberIoann < enemyNumber:
                                IoannStronk -= 1
                            numberIoann -= enemyNumber
                        else:
                            numberIoann = 0
                        if enemyNumber > 0:
                            enemyNumber -= numberIoann
                            if enemyNumber < numberIoann:
                                enemyStroke -= 1
                        isDamage = False
                    isCancleIoann = False
                    characterAttack = 4
                elif characterAttack == 3:
                    if not isShieldValeria:
                        if numberValeria > 0:
                            if numberValeria < enemyNumber:
                                ValeriaStonk -= 1
                            numberValeria -= enemyNumber
                        else:
                            numberValeria = 0
                        if enemyNumber > 0:
                            enemyNumber -= numberValeria
                            if enemyNumber < numberValeria:
                                enemyStroke -= 1
                        isDamage = False
                    isCancleValeria = False
                    characterAttack = 4
                if characterAttack == 4:
                    if enemyStroke >= 0:
                        isAnimTXT = True
                        enemyNumber = random.randint(5, 35)
                    numberValeria = 1
                    numberIoann = 1
                    numberAnna = 1
                    isShieldValeria = False
                    selectCube = 0
                    isShieldIoann = False
                    isShieldAnna = False
                    selectCharacter = 1
                    isDamage = False
                    isStart = False
                    characterAttack = random.randint(1, 3)
            else:
                if timeDamge == 15:
                    timeDamge = 0
                    isDamage = True
                timeDamge += 1
        sc.fill((0, 0, 0))
        sc.blit(backImage, backRect)
        if selectCharacter == 1:
            arowRect.y = 85
            sc.blit(arowImage, arowRect)
        if selectCharacter == 2:
            arowRect.y = 230
            sc.blit(arowImage, arowRect)
        if selectCharacter == 3:
            arowRect.y = 375
            sc.blit(arowImage, arowRect)
        sc.blit(numberCube, numberRect)
        sc.blit(shieldCube, shieldRect)
        sc.blit(shieldTXT, shieldTRect)
        sc.blit(CancleCube, CancleRect)
        sc.blit(Frame1, Frame1Rect)
        sc.blit(StartImage, StartRect)
        sc.blit(KeyZ, KeyZRect)
        sc.blit(KeyF, KeyFRect)
        sc.blit(KeyB, KeyBRect)
        sc.blit(KeyI, KeyIRect)
        sc.blit(ConfirmTXT, ConfirmTXTRect)
        sc.blit(KeyJ, KeyJRect)
        sc.blit(ValeriaUI, ValeriaRect)
        sc.blit(AnnaUI, AnnaRect)
        sc.blit(IoannUI, IoannRect)
        sc.blit(enemyBandit, banditRect)
        if characterAttack == 1:
            swordRect = swordIcon.get_rect(center=(165, 18))
            sc.blit(swordIcon, swordRect)
        if characterAttack == 2:
            swordRect = swordIcon.get_rect(center=(165, 175))
            sc.blit(swordIcon, swordRect)
        if characterAttack == 3:
            swordRect = swordIcon.get_rect(center=(165, 330))
            sc.blit(swordIcon, swordRect)

        if enemyStroke > 0:
            sc.blit(ememyNumberTXT, enemyNumberRect)
        if isShieldAnna:
            shieldIRect = shieldIcon.get_rect(center=(300, 105))
            sc.blit(shieldIcon, shieldIRect)
        if isShieldIoann:
            shieldIRect = shieldIcon.get_rect(center=(300, 255))
            sc.blit(shieldIcon, shieldIRect)
        if isShieldValeria:
            shieldIRect = shieldIcon.get_rect(center=(300, 405))
            sc.blit(shieldIcon, shieldIRect)
        if isCancleAnna:
            cancleIRect = cancleIcon.get_rect(center=(300, 105))
            sc.blit(cancleIcon, cancleIRect)
        if isCancleIoann:
            cancleIRect = cancleIcon.get_rect(center=(300, 255))
            sc.blit(cancleIcon, cancleIRect)
        if isCancleValeria:
            cancleIRect = cancleIcon.get_rect(center=(300, 405))
            sc.blit(cancleIcon, cancleIRect)
        if numberAnna > 0 and not isShieldAnna and not isCancleAnna:
            sc.blit(numberAnnaText, numberARect)
        if numberIoann > 0 and not isShieldIoann and not isCancleIoann:
            sc.blit(numberIoannText, numberIRect)
        if numberValeria > 0 and not isShieldValeria and not isCancleValeria:
            sc.blit(numberValeriaText, numberVRect)
        pygame.display.update()
        clock.tick(FPS)

def nextLevel():
    global level
    running = True
    FPS = 60

    backGround = pygame.image.load('sprite/ui/back.png').convert_alpha()
    backGround = pygame.transform.scale(backGround, (RES[0], RES[1]))
    backRect = backGround.get_rect(center=(RES[0]//2, RES[1]//2))


    ui1 = pygame.image.load('sprite/ui/1.png').convert_alpha()
    ui1 = pygame.transform.scale(ui1, (482, 482))
    ui1.set_alpha(250)
    ui1Rect = ui1.get_rect(center=(RES[0]//2, RES[1]//2))

    KeyJ = pygame.image.load('sprite/ui/keyboard/J.png').convert_alpha()
    KeyJ = pygame.transform.scale(KeyJ, (32, 32))
    KeyJRect = KeyJ.get_rect(center=(RES[0]//2+110, RES[1]//2-50))

    fontText = pygame.font.Font('Font/2.ttf', 30)
    TXT1 = fontText.render('Excellent :)', False, (255, 255, 0))
    TXT1Rect = TXT1.get_rect(center=(RES[0]//2, RES[1]//2-135))


    fontText2 = pygame.font.Font('Font/1.ttf', 25)
    TXTContinue = fontText2.render('Continue', False, (255, 255, 255))
    TXTContinueRect = TXTContinue.get_rect(center=(RES[0]//2+110, RES[1]//2-10))

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_j:
                    level += 1
                    running = False
                    switch_scene(sceneGame)
        sc.fill((0, 0, 0))
        sc.blit(backGround, backRect)
        sc.blit(ui1, ui1Rect)
        sc.blit(TXT1, TXT1Rect)
        sc.blit(TXTContinue, TXTContinueRect)
        sc.blit(KeyJ, KeyJRect)
        pygame.display.update()
        clock.tick(FPS)

def infoScreen():
    running = True
    FPS = 60

    page = 0

    howToPlayFont = pygame.font.Font('Font/2.ttf', 45)
    howToPlay = howToPlayFont.render('How To Play', False, (255, 255, 255))
    HowToRect = howToPlay.get_rect(center=(RES[0]//2, RES[1]//2-370))

    font1 = pygame.font.Font('Font/5.ttf', 25)

    TXT = font1.render('This is the playing field', False, (255, 255, 0))
    TXTRect = TXT.get_rect(center=(150, 530))

    TXT2 = font1.render('This is the playing field', False, (255, 255, 0))
    TXT2Rect = TXT2.get_rect(center=(150, 560))

    screenShot = pygame.image.load('sprite/screen/1.png').convert_alpha()
    screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
    screenShotRect = screenShot.get_rect(center=(RES[0]//2+255, RES[1]//2))

    frameScreen = 0

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            if e.type == pygame.KEYDOWN:
                page += 1
        sc.fill((0, 0, 0))
        if page == 0:
            screenShot = pygame.image.load('sprite/screen/1.png').convert_alpha()
            screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            TXT = font1.render('This is the playing field', False, (255, 255, 0))
        if page == 1:
            if frameScreen == 40:
                frameScreen = 0
                screenShot = pygame.image.load('sprite/screen/1.png').convert_alpha()
                screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            if frameScreen == 10:
                screenShot = pygame.image.load('sprite/screen/2.png').convert_alpha()
                screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            if frameScreen == 20:
                screenShot = pygame.image.load('sprite/screen/3.png').convert_alpha()
                screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            if frameScreen == 30:
                screenShot = pygame.image.load('sprite/screen/4.png').convert_alpha()
                screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            frameScreen += 1
            TXT = font1.render('F, B, J keys select action', False, (255, 255, 0))
        if page == 2:
            if frameScreen == 40:
                frameScreen = 0
                screenShot = pygame.image.load('sprite/screen/1.png').convert_alpha()
                screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            if frameScreen == 10:
                screenShot = pygame.image.load('sprite/screen/2.png').convert_alpha()
                screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            if frameScreen == 20:
                screenShot = pygame.image.load('sprite/screen/3.png').convert_alpha()
                screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            if frameScreen == 30:
                screenShot = pygame.image.load('sprite/screen/4.png').convert_alpha()
                screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            frameScreen += 1
            TXT = font1.render('F = Choice of number', False, (255, 255, 0))
        if page == 3:
            if frameScreen == 40:
                frameScreen = 0
                screenShot = pygame.image.load('sprite/screen/1.png').convert_alpha()
                screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            if frameScreen == 10:
                screenShot = pygame.image.load('sprite/screen/2.png').convert_alpha()
                screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            if frameScreen == 20:
                screenShot = pygame.image.load('sprite/screen/3.png').convert_alpha()
                screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            if frameScreen == 30:
                screenShot = pygame.image.load('sprite/screen/4.png').convert_alpha()
                screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            frameScreen += 1
            TXT = font1.render('B = Activate Shield', False, (255, 255, 0))
        if page == 4:
            if frameScreen == 40:
                frameScreen = 0
                screenShot = pygame.image.load('sprite/screen/1.png').convert_alpha()
                screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            if frameScreen == 10:
                screenShot = pygame.image.load('sprite/screen/2.png').convert_alpha()
                screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            if frameScreen == 20:
                screenShot = pygame.image.load('sprite/screen/3.png').convert_alpha()
                screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            if frameScreen == 30:
                screenShot = pygame.image.load('sprite/screen/4.png').convert_alpha()
                screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            frameScreen += 1
            TXT = font1.render('J = Skip a turn', False, (255, 255, 0))
        if page == 5:
            if frameScreen == 30:
                frameScreen = 0
                screenShot = pygame.image.load('sprite/screen/1.png').convert_alpha()
                screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            if frameScreen == 10:
                screenShot = pygame.image.load('sprite/screen/5.png').convert_alpha()
                screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            frameScreen += 1
            sc.blit(TXT2, TXT2Rect)
            TXT2 = font1.render('press the I key to confirm the action', False, (255, 255, 0))
            TXT = font1.render('After choosing an action', False, (255, 255, 0))
        if page == 6:
            screenShot = pygame.image.load('sprite/screen/6.png').convert_alpha()
            screenShot = pygame.transform.smoothscale(screenShot, (645, 265))
            TXT = font1.render('If you see a sword icon on a character', False, (255, 255, 0))
        if page == 7:
            screenShot = pygame.image.load('sprite/screen/1.png').convert_alpha()
            screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            TXT = font1.render("When you're ready, press the Z key to start", False, (255, 255, 0))
        if page == 8:
            screenShot = pygame.image.load('sprite/screen/1.png').convert_alpha()
            screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            sc.blit(TXT2, TXT2Rect)
            TXT2 = font1.render('then the opponent will have fewer moves', False, (255, 255, 0))
            TXT = font1.render("If the opponent's number is less than yours,", False, (255, 255, 0))
        if page == 9:
            screenShot = pygame.image.load('sprite/screen/7.png').convert_alpha()
            screenShot = pygame.transform.smoothscale(screenShot, (645, 265))
            TXT = font1.render("If the enemy has no moves then you win", False, (255, 255, 0))
        if page == 10:
            screenShot = pygame.image.load('sprite/screen/1.png').convert_alpha()
            screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            TXT = font1.render("Same with your characters.", False, (255, 255, 0))
        if page == 11:
            screenShot = pygame.image.load('sprite/screen/1.png').convert_alpha()
            screenShot = pygame.transform.smoothscale(screenShot, (745, 465))
            TXT = font1.render("Good luck", False, (255, 255, 0))
        if page == 13:
            running = False
            switch_scene(mainMenu)
        sc.blit(screenShot, screenShotRect)
        sc.blit(TXT, TXTRect)
        sc.blit(howToPlay, HowToRect)
        pygame.display.update()
        clock.tick(FPS)

def mainMenu():
    running = True
    FPS = 60

    select = pygame.mixer.Sound('Audio/SFX/blipSelect.wav')

    BlockPlay = pygame.image.load('sprite/ui/cube/gamepad.png').convert_alpha()
    BlockPlay = pygame.transform.scale(BlockPlay, (358, 358))
    BlockPlayRect = BlockPlay.get_rect(center=(300, RES[1]//2+250))

    BlockInfo = pygame.image.load('sprite/ui/cube/Info.png').convert_alpha()
    BlockInfo = pygame.transform.scale(BlockInfo, (358, 358))
    BlockInfoRect = BlockInfo.get_rect(center=(RES[0]//2, RES[1]//2+250))

    BlockQuit = pygame.image.load('sprite/ui/cube/Quit.png').convert_alpha()
    BlockQuit = pygame.transform.scale(BlockQuit, (358, 358))
    BlockQuitRect = BlockQuit.get_rect(center=(RES[0]//2+350, RES[1]//2+250))

    KeyF = pygame.image.load('sprite/ui/keyboard/F.png').convert_alpha()
    KeyF = pygame.transform.scale(KeyF, (42, 42))
    KeyFRect = KeyF.get_rect(center=(BlockPlayRect.x+190, BlockPlayRect.y+55))

    KeyB = pygame.image.load('sprite/ui/keyboard/B.png').convert_alpha()
    KeyB = pygame.transform.scale(KeyB, (42, 42))
    KeyBRect = KeyB.get_rect(center=(RES[0]//2-5, RES[1]//2+150))

    KeyJ = pygame.image.load('sprite/ui/keyboard/J.png').convert_alpha()
    KeyJ = pygame.transform.scale(KeyJ, (42, 42))
    KeyJRect = KeyJ.get_rect(center=(RES[0]//2+340, RES[1]//2+130))

    background = pygame.image.load('sprite/ui/menuBackNight.png').convert_alpha()
    background = pygame.transform.scale(background, (RES[0], RES[1]+350))
    background.set_alpha(195)
    backRectGround = background.get_rect(center=(RES[0]//2, RES[1]//2))

    GameLogo = pygame.image.load('sprite/ui/GameLogo.png').convert_alpha()
    GameLogo = pygame.transform.scale(GameLogo, (228, 228))
    yPos = RES[1]//2-540
    GameRect = GameLogo.get_rect(center=(RES[0]//2, yPos))

    FrameLogo = 0

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_f:
                    select.play()
                    running = False
                    switch_scene(sceneGame)
                if e.key == pygame.K_b:
                    select.play()
                    running = False
                    switch_scene(infoScreen)
                if e.key == pygame.K_j:
                    select.play()
                    running = False
                    switch_scene(None)
        sc.fill((0, 0 ,0))
        if FrameLogo < 35:
            yPos += 5
            GameRect = GameLogo.get_rect(center=(RES[0]//2, yPos))
            FrameLogo += 1
        sc.blit(background, backRectGround)
        sc.blit(GameLogo, GameRect)
        sc.blit(BlockPlay, BlockPlayRect)
        sc.blit(BlockQuit, BlockQuitRect)
        sc.blit(BlockInfo, BlockInfoRect)
        sc.blit(KeyF, KeyFRect)
        sc.blit(KeyB, KeyBRect)
        sc.blit(KeyJ, KeyJRect)
        pygame.display.update()
        clock.tick(FPS)

def dialog1():
    running = True
    FPS = 60

    FontTXTD = pygame.font.Font('Font/2.ttf', 35)
    TxtD = FontTXTD.render('what?', False, (0, 255, 0))
    TXTrect = TxtD.get_rect(center=(RES[0]//2-560, RES[1]//2+380))

    alphaTXT = 500
    TxtD.set_alpha(alphaTXT)

    select = 0

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
            if e.type == pygame.KEYDOWN:
                select += 1
        if select == 0:
            TxtD = FontTXTD.render('what?', False, (0, 255, 0))
        if select == 1:
            TxtD = FontTXTD.render('WHAT?!', False, (0, 255, 0))
        if select == 2:
            TxtD = FontTXTD.render('Why am I alive?', False, (0, 255, 0))
        if select == 3:
            TxtD = FontTXTD.render('...', False, (139, 0, 235))
        if select == 4:
            TxtD = FontTXTD.render('I felt sorry for killing you', False, (139, 0, 235))
        if select == 5:
            TxtD = FontTXTD.render('And not only you', False, (139, 0, 235))
        if select == 6:
            TxtD = FontTXTD.render('what the fuck', False, (0, 255, 0))
        if select == 7:
            TxtD = FontTXTD.render("I don't want people who are dear to me to die at my hands. I want peace and tranquility", False, (139, 0, 235))
        if select == 8:
            TxtD = FontTXTD.render('Forgive me', False, (139, 0, 235))
        if select == 9:
            TxtD = FontTXTD.render('Ahh listen you are a great friend and I understand this again and again', False, (0, 255, 0))
        if select == 10:
            TxtD = FontTXTD.render('But in return, I want the three of you to kill a wasabi tarantula', False, (139, 0, 235))
        if select == 11:
            TxtD = FontTXTD.render('Kill him I bless you', False, (139, 0, 235))
        if select == 12:
            TxtD = FontTXTD.render("If he doesn't die, you will become torture toys.", False, (139, 0, 235))
        if select >= 13:
            alphaTXT -= 3
            TxtD.set_alpha(alphaTXT)
            if alphaTXT < -100:
                running = False
                switch_scene(mainMenu)
        sc.fill((0, 0 , 0))
        sc.blit(TxtD, TXTrect)
        pygame.display.update()
        clock.tick(FPS)

def createScreen():
    running = True
    FPS = 60

    FrameTitle = 0
    Alpha = 0
    Alpha2 = 0

    FrameJam = 0
    isJam = False

    fontTextJam = pygame.font.Font('Font/7.ttf', 45)
    MiniJam = fontTextJam.render('Mini Jam 116: Pocket Sized', False, (0, 255, 0))
    MiniJam.set_alpha(0)
    miniJamRect = MiniJam.get_rect(center=(RES[0]//2+5, RES[1]//2))

    jamIcon = pygame.image.load('sprite/ui/jamIcon.png').convert_alpha()
    jamIcon = pygame.transform.scale(jamIcon, (128, 128))
    jamIcon.set_alpha(-5)
    jamRect = jamIcon.get_rect(center=(RES[0]//2-350, RES[1]//2-15))

    FontTitle = pygame.font.Font('Font/5.ttf', 55)
    TitleChan = FontTitle.render('TitleChanQWERTY', False, (139, 0, 235))
    TitleChan.set_alpha(0)
    TitleChanRect = TitleChan.get_rect(center=(RES[0]//2, RES[1]//2))



    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                switch_scene(None)
        sc.fill((0, 0 ,0))
        if FrameTitle < 240:
            Alpha += 2
            TitleChan.set_alpha(Alpha)
        if FrameTitle > 240:
            Alpha -= 2
            TitleChan.set_alpha(Alpha)
        if FrameTitle > 520:
            FrameJam += 1
            isJam = True
        FrameTitle += 1
        sc.blit(TitleChan, TitleChanRect)
        sc.blit(MiniJam, miniJamRect)
        sc.blit(jamIcon, jamRect)
        if FrameJam < 240 and isJam:
            Alpha2 += 2
            jamIcon.set_alpha(Alpha2)
            MiniJam.set_alpha(Alpha2)
        if FrameJam > 240:
            Alpha2 -= 2
            jamIcon.set_alpha(Alpha2)
            MiniJam.set_alpha(Alpha2)
        if FrameJam > 550:
            running = False
            switch_scene(dialog1)
        pygame.display.update()
        clock.tick(FPS)

switch_scene(createScreen)
while curent_scene is not None:
    curent_scene()
    clock.tick(60)

pygame.quit()
