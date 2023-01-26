import streamlit as st
import webbrowser

# lol
rickroll = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# summoner links
smn_two_48 = "https://etro.gg/gearset/b3567b2d-5c92-4ba1-a18a-eb91b614e944"
smn_two_47 = "https://etro.gg/gearset/42575c18-b518-473d-a082-efdc580f0ec2"
smn_two_46 = "https://etro.gg/gearset/750617ed-aad2-42a0-b68a-1f59b2ea035f"
smn_two_45 = "https://etro.gg/gearset/bb37ef05-9cd3-498d-889b-dcc4934fc4bf"
smn_two_19 = "https://etro.gg/gearset/cd0105ef-f8fb-4dca-aeb2-7853db4ad27a"
smn_two_18 = "https://etro.gg/gearset/58739dc7-c265-4874-90e5-dd875eb29dad"
# rdm links
rdm_bis = "https://etro.gg/gearset/5f972eb8-c3cd-44da-aa73-0fa769957e5b"
# blm links
blm_22_87 = "https://etro.gg/gearset/bd1b7a52-5893-4928-9d7c-d47aea22d8d2"
blm_12_92 = "https://etro.gg/gearset/12deb5db-9f38-42e1-bdba-f8be8ddcb97d"
blm_84_0 = "https://etro.gg/gearset/73f9f3af-2fa1-4871-85a3-a0f6adbb5e28"
# brd link
brd_bis = "https://etro.gg/gearset/2a242f9b-8a41-4d09-9e14-3c8fb08e97e4"
# dnc link
dnc_bis = "https://etro.gg/gearset/fb5976d5-a94c-4052-9092-3c3990fefa76"
# mch link
mch_247 = "https://etro.gg/gearset/d48aaab2-102d-4b29-aa58-f1d7eb035fa0"
mch_250 = "https://etro.gg/gearset/8a0bdf80-80f5-42e8-b10a-160b0fc2d151"
# drg
drg_250 = "https://etro.gg/gearset/de153cb0-05e7-4f23-a924-1fc28c7ae8db"
drg_246 = "https://etro.gg/gearset/d723087d-3d5b-4c77-9b59-f925c15d294c"
# sam
sam_215 = "https://etro.gg/gearset/4356046d-2f05-432a-a98c-632f11098ade"
sam_208 = "https://etro.gg/gearset/56e084de-6194-45a5-8af7-6834f902f791"
sam_200 = "https://etro.gg/gearset/c7601428-cf57-456b-a2ed-321fd2c25ff7"
# rpr
rpr_250 = "https://etro.gg/gearset/00b6b315-5807-4238-9164-428ab3dedeaa"
rpr_249 = "https://etro.gg/gearset/c293f73b-5c58-4855-b43d-aae55b212611"
# mnk
mnk_1941 = "https://etro.gg/gearset/3ab677f7-9934-4578-aa3f-553344d35421"
mnk_193 = "https://etro.gg/gearset/53ef792e-7e35-4ff4-80f2-476e646cd986"
mnk_1942 = "https://etro.gg/gearset/337dbe69-cce9-4b33-9f04-92554b729e2e"
# ninja
nin_210 = "https://etro.gg/gearset/c0c2ba50-b93a-4d18-8cba-a0ebb0705fed"
nin_212 = "https://etro.gg/gearset/9e07d761-8105-4ee5-9921-8f35d8b4a631"


st.set_page_config(layout="centered")
col1, col2, col3 = st.columns(3, gap="small")

with col1:
    st.subheader("**Role**")
    if "magic_role" not in st.session_state:
        st.session_state["magic_role"] = False
    if "physical_role" not in st.session_state:
        st.session_state["physical_role"] = False
    if "melee_role" not in st.session_state:
        st.session_state["melee_role"] = False

    caster = st.button("**Magical Ranged DPS**")
    phys = st.button("Physical Ranged DPS")
    melee = st.button("Melee DPS")
    if caster:
        st.session_state["magic_role"] = True
        st.session_state["physical_role"] = False
        st.session_state["melee_role"] = False
    elif phys:
        st.session_state["physical_role"] = True
        st.session_state["magic_role"] = False
        st.session_state["melee_role"] = False
    elif melee:
        st.session_state["melee_role"] = True
        st.session_state["magic_role"] = False
        st.session_state["physical_role"] = False

# Caster
if st.session_state["magic_role"]:
    with col2:
        st.subheader("**Job**")
        smn = st.button("**Summoner**")
        blm = st.button("**Black Mage**")
        rdm = st.button("**Red Mage**")

        if "summoner" not in st.session_state:
            st.session_state["summoner"] = False
        if "red_mage" not in st.session_state:
            st.session_state["red_mage"] = False
        if "black_mage" not in st.session_state:
            st.session_state["black_mage"] = False

    if smn:
        st.session_state["summoner"] = True
        st.session_state["red_mage"] = False
        st.session_state["black_mage"] = False

    if rdm:
        st.session_state["red_mage"] = True
        st.session_state["summoner"] = False
        st.session_state["black_mage"] = False

    if blm:
        st.session_state["black_mage"] = True
        st.session_state["red_mage"] = False
        st.session_state["summoner"] = False

if st.session_state["magic_role"] and st.session_state["summoner"]:
    with col3:
        st.subheader("**Crit BIS**")

        smn_2_48 = st.button("2.48")
        if smn_2_48:
            webbrowser.open_new_tab(smn_two_48)
        smn_2_47 = st.button("2.47")
        if smn_2_47:
            webbrowser.open_new_tab(smn_two_47)
        smn_2_46 = st.button("2.46")
        if smn_2_46:
            webbrowser.open_new_tab(smn_two_46)
        smn_2_45 = st.button("2.45")
        if smn_2_45:
            webbrowser.open_new_tab(smn_two_45)

    with col3:
        st.markdown("")
        st.subheader("**SPS BIS**")
        smn_2_19 = st.button("2.19")
        if smn_2_19:
            webbrowser.open_new_tab(smn_two_19)
        smn_2_18 = st.button("2.18")
        if smn_2_18:
            webbrowser.open_new_tab(smn_two_18)

    with col3:
        st.markdown("")
        st.subheader("**Ez Rank 1**")
        lol = st.button("1.01")
        if lol:
            webbrowser.open_new_tab(rickroll)

if st.session_state["magic_role"] and st.session_state["black_mage"]:
    with col3:
        st.subheader("**Crit BIS**")
        blm_1292 = st.button("1292 SPS")
        if blm_1292:
            webbrowser.open_new_tab(blm_12_92)
        blm_840 = st.button("840 SPS")
        if blm_840:
            webbrowser.open_new_tab(blm_84_0)
    with col3:
        st.markdown("")
        st.subheader("**SPS BIS**")
        blm_2287 = st.button("2287 SPS")
        if blm_2287:
            webbrowser.open_new_tab(blm_22_87)

if st.session_state["magic_role"] and st.session_state["red_mage"]:
    with col3:
        st.subheader("**Rdm BIS**")
        if "rdm_2.48" not in st.session_state:
            st.session_state["rdm_2.48"] = False
        rdm_248 = st.button("2.48")
        if rdm_248:
            webbrowser.open_new_tab(rdm_bis)

# Physical
if st.session_state["physical_role"]:
    with col2:
        st.subheader("Job")
        brd = st.button("Bard")
        dnc = st.button("Dancer")
        mch = st.button("Machinist")

        if "bard" not in st.session_state:
            st.session_state["bard"] = False
        if "dancer" not in st.session_state:
            st.session_state["dancer"] = False
        if "machinist" not in st.session_state:
            st.session_state["machinist"] = False

    if brd:
        st.session_state["bard"] = True
        st.session_state["dancer"] = False
        st.session_state["machinist"] = False
    if dnc:
        st.session_state["dancer"] = True
        st.session_state["bard"] = False
        st.session_state["machinist"] = False
    if mch:
        st.session_state["machinist"] = True
        st.session_state["bard"] = False
        st.session_state["dancer"] = False

if st.session_state["physical_role"] and st.session_state["bard"]:
    with col3:
        st.subheader("**Bard BIS**")
        brd_247 = st.button("2.47")
        if "bard_bis" not in st.session_state:
            st.session_state["bard_bis"] = False
        if brd_247:
            webbrowser.open(brd_bis)

if st.session_state["physical_role"] and st.session_state["dancer"]:
    with col3:
        st.subheader("**Dancer BIS**")
        dnc_247 = st.button("2.47")
        if "bard_bis" not in st.session_state:
            st.session_state["dnc_bis"] = False
        if dnc_247:
            webbrowser.open(dnc_bis)

if st.session_state["physical_role"] and st.session_state["machinist"]:
    with col3:
        st.subheader("**Machinist BIS**")
        mch_two_47 = st.button("2.47")
        mch_two_50 = st.button("2.50")
        if "mch247" not in st.session_state:
            st.session_state["mch247"] = False
        if "mch250" not in st.session_state:
            st.session_state["mch250"] = False
        if mch_two_47:
            webbrowser.open(mch_247)
        if mch_two_50:
            webbrowser.open(mch_250)

# Melee

if st.session_state["melee_role"]:
    with col2:
        st.subheader("**Job**")
        drg = st.button("**Dragoon**")
        sam = st.button("**Samurai**")
        rpr = st.button("**Reaper**")
        mnk = st.button("**Monk**")
        nin = st.button("**Ninja**")

        if "dragoon" not in st.session_state:
            st.session_state["dragoon"] = False
        if "samurai" not in st.session_state:
            st.session_state["samurai"] = False
        if "reaper" not in st.session_state:
            st.session_state["reaper"] = False
        if "monk" not in st.session_state:
            st.session_state["monk"] = False
        if "ninja" not in st.session_state:
            st.session_state["ninja"] = False

    if drg:
        st.session_state["dragoon"] = True
        st.session_state["samurai"] = False
        st.session_state["reaper"] = False
        st.session_state["monk"] = False
        st.session_state["ninja"] = False

    if sam:
        st.session_state["samurai"] = True
        st.session_state["dragoon"] = False
        st.session_state["reaper"] = False
        st.session_state["monk"] = False
        st.session_state["ninja"] = False

    if rpr:
        st.session_state["reaper"] = True
        st.session_state["samurai"] = False
        st.session_state["dragoon"] = False
        st.session_state["monk"] = False
        st.session_state["ninja"] = False

    if mnk:
        st.session_state["monk"] = True
        st.session_state["samurai"] = False
        st.session_state["dragoon"] = False
        st.session_state["reaper"] = False
        st.session_state["ninja"] = False

    if nin:
        st.session_state["ninja"] = True
        st.session_state["monk"] = False
        st.session_state["samurai"] = False
        st.session_state["dragoon"] = False
        st.session_state["reaper"] = False

if st.session_state["melee_role"] and st.session_state["dragoon"]:
    with col3:
        st.subheader("Drg BIS")
        drg250 = st.button("2.50")
        drg246 = st.button("2.46")
        if "drg250" not in st.session_state:
            st.session_state["drg250"] = False
        if "drg246" not in st.session_state:
            st.session_state["drg246"] = False

    if drg250:
        webbrowser.open(drg_250)
    if drg246:
        webbrowser.open(drg_246)

if st.session_state["melee_role"] and st.session_state["samurai"]:
    with col3:
        st.subheader("Sam BIS")
        sam215 = st.button("2.15")
        sam208 = st.button("2.08")
        sam200 = st.button("2.00")
        if "sam215" not in st.session_state:
            st.session_state["sam125"] = False
        if "sam208" not in st.session_state:
            st.session_state["sam208"] = False
        if "sam200" not in st.session_state:
            st.session_state["sam200"] = False

    if sam215:
        webbrowser.open(sam_215)
    if sam208:
        webbrowser.open(sam_208)
    if sam200:
        webbrowser.open(sam_200)

if st.session_state["melee_role"] and st.session_state["reaper"]:
    with col3:
        st.subheader("Rpr BIS")
        rpr250 = st.button("2.50")
        rpr249 = st.button("2.49")
        if "rpr250" not in st.session_state:
            st.session_state["rpr250"] = False
        if "rpr249" not in st.session_state:
            st.session_state["rpr249"] = False

        if rpr250:
            webbrowser.open(rpr_250)
        if rpr249:
            webbrowser.open(rpr_249)

if st.session_state["melee_role"] and st.session_state["monk"]:
    with col3:
        st.subheader("Mnk BIS")
        mnk1941 = st.button("1.94", key="mnk1")
        mnk193 = st.button("1.93")
        mnk1942 = st.button("1.94", key="mnk2")
        if "mnk1941" not in st.session_state:
            st.session_state["mnk1941"] = False
        if "mnk193" not in st.session_state:
            st.session_state["mnk193"] = False
        if "mnk1942" not in st.session_state:
            st.session_state["mnk1942"] = False

    if mnk1941:
        webbrowser.open(mnk_1941)
    if mnk193:
        webbrowser.open(mnk_193)
    if mnk1942:
        webbrowser.open(mnk_1942)

if st.session_state["melee_role"] and st.session_state["ninja"]:
    with col3:
        st.subheader("Nin BIS")
        nin210 = st.button("2.10")
        nin212 = st.button("2.12")
        if "nin210" not in st.session_state:
            st.session_state["nin210"] = False
        if "nin212" not in st.session_state:
            st.session_state["nin212"] = False

        if nin210:
            webbrowser.open(nin_210)
        if nin212:
            webbrowser.open(nin_212)




