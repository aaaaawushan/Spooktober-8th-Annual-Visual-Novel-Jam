# ========== 角色定义 ==========

define i = Character("Iris", color="#8b4343", image="iris")
define ii = Character("Iris", color="#8b4343")
define e = Character("Elena", color="#ffcc00", image="elena")
define l = Character("Lydia", color="#88ccff", image="lydia")
define cult = Character("教团成员", color="#aaaaaa")

# ========== 界面定义 ==========

screen phone_sns():
    add "images/ui/phone_frame.png" align (0.5, 0.5)
    frame:
        xalign 0.5 yalign 0.5
        xsize 400 ysize 600
        background None
        vbox:
            spacing 20
            textbutton "Elena：嘿，我听说你和Alen的事，你还好吗？...":
                text_size 20
                text_color "#000000"
                action Return("elena_msg")
            text "Alen：我已经提交了离婚申请，你…" size 20 color "#888888"

# ========== 游戏开始 ==========

label start:
    $ replied_elena = False
    jump scene_1_1

# ========== 场景1-1：仪式进行中 ==========

label scene_1_1:
    # play music "audio/bgm_ritual.ogg"

    scene cg_1 with dissolve
    pause
    scene cg_2 with dissolve
    pause
    scene cg_3 with dissolve
    pause
    ii "只要这么做了我就可以……"

    # play sound "audio/sfx_stab.ogg"
    # stop music fadeout 1.0

    scene black with Dissolve(1.5)

    jump scene_2_1

# ========== 场景2-1：一切开始前 ==========

label scene_2_1:
    # play music "audio/bgm_memory_slow.ogg"
    scene bg_room with dissolve

    show side iris frowning
    i "呃……头好痛……好饿……我得去找点吃的……"

    # play sound "audio/sfx_phone_vibrate.ogg"

    call screen phone_sns

    jump after_phone

# ========== 手机互动后 ==========

label after_phone:
    show side iris sad

    menu:
        "回复Elena消息":
            $ replied_elena = True
            i "呃…我一切都好！我现在很忙所以没什么时间联系你，你知道的，工作啊搬家，都太花精力了，说起来你和和父亲关系还好吗！我希望一切都好，哈哈总之不用担心我，我很好！"
            show side iris sad
            i "天啊我都发了些什么…真是蠢货，白痴，没用，呃，我真是个废物.."
        "不回复":
            $ replied_elena = False

    i "{i}为什么还要在乎我…为什么还要关心我……我根本不值得这些……{/i}"

    # jump scene_2_1_lydia

    return