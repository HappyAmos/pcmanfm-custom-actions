#!/bin/bash
    #
    #
    # md5sum-mint 0.1 created by shane <linuxmint.com>
    # This program is free software; you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation; either version 2 of the License, or
    # (at your option) any later version.
    #
    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.
    #
    # You should have received a copy of the GNU General Public License
    # along with this program; if not, write to the Free Software
    # Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  
    # USA
    # dependencies
    #       bash
    #       zenity
     
    ################################################
    #               TRANSLATIONS
    #-----------------------------------------------
    #       Default = English
    title="MD5 Checksum                     "
    title1="MD5 Checksum - Select a file    "
    title2="MD5 Checksum - Error            "
    text1="Select a file"
    text2="Calculating MD5 Checksum...   "
    text3="MD5 Checksum aborted"
    text4="The MD5 Checksum is:"
    text5="The md5sum file is:"
    text6="<b>Select the actions you wish to perform</b>"
    error1="You do not have read permission"
    error2="You do not have write permission"
    error3="No action selected. Exiting."
    action0="Action"
    action1="Display the calculated md5sum"
    action2="Save the md5sum to a file"
    case $LANG in
            ######## Japanese by blowback ########
            ja* )
                    title="MD5チェックサム                     "
                    title1="MD5チェックサム - ファイルの選択    "
                    title2="MD5チェックサム - エラー           "
                    text1="ファイルの選択"
                    text2="MD5チェックサムを計算しています...   "
                    text3="MD5チェックサムが中止されました"
                    text4="MD5チェックサム:"
                    text5="md5sumファイル:"
                    text6="<b>実行したいアクションを選んでください</b>"
                    error1="読み込み権がありません"
                    error2="書き込み権がありません"
                    error3="アクションが選択されていません。終了します。"
                    action0="アクション"
                    action1="計算したmd5sumを表示"
                    action2="md5sumをファイルに保存"
    esac
    ################################################
     
    #Check if running under X
    xcheck=`tty | cut -d '/' -f3`
    if [ $xcheck != "pts" ]
    then
            echo "Error: md5sum-mint must be run under X"
            exit 1
    fi
     
    #If no file is selected
    if [ -z "$1" ]
    then
            cd $HOME
            input=$(zenity --file-selection --title="$title1")
    else
    #If a file is selected
            if [ -f "$1" ]
            then
                    input="$1"
            else
    #If a directory is selected
                    cd "$1"
                    input=$(zenity --file-selection --title="$title1")
            fi
    fi
     
    #If still no file is selected (operation cancelled)
    if [ -z "$input" ]
    then
            exit 1
    fi
     
    #Check read permissions for input file
    if [ ! -r "$input" ]
    then
            zenity --error --title="$title" --text "<b>$input:</b>
     
    $error1"
            exit 2
    fi
     
    #Get location and filename from input
    wdir=`dirname "$input"`
    file=`basename "$input"`
     
    #cd into directory
    cd "$wdir"
     
    #debug
    #zenity --info --text "Debug:
    #dir is $wdir
    #file is $file"
     
    #Actions selection dialog
    action=$(zenity --list --title="$title" --text "$text6" --checklist --column "" --column "$action0" TRUE "$action1" FALSE "$action2" --separator=":")
     
    #debug
    #zenity --info --text "Debug:
    #$action ."
     
    #If no action selected
    if [ -z "$action" ]
    then
            zenity --error --title="$title2" --text "$error3"
            exit 3
    fi
     
    #Check if saving to file is selected
    if [ "$action" != "$action1" ]
    then
     
    #Check write permission to directory
            if [ ! -w "$wdir" ]
            then
                    zenity --error --title="$title2" --text "<b>$wdir:</b>
     
    $error2"
                    exit 4
            fi
    fi
     
    #debug
    #zenity --info --text "Debug:
    #$action"
     
    #Calculate md5sum, progress dialog and output to file
    md5sum "$file" | tee >(cut -d ' ' -f1 > /tmp/sum) | (zenity --progress --title="$title" --pulsate --auto-kill --auto-close --text "$text2")
     
    #Find the zenity progress dialog
    running=`ps aux | grep "$text2" | sed '/grep/ d'`
     
    #Loop while progress dialog is running
    until [ -z "$running" ]
    do
            sleep 1
            running=`ps aux | grep "$text2" | sed '/grep/ d'`
    done
     
    #Check if md5sum is still running after zenity dialog has closed
     
    sum=`cat /tmp/sum`
    rm /tmp/sum
     http://pastebin.com/RpWHWpEe
    #debug
    #zenity --info --text "Debug:
    #$sum"
     
    #Completed successfully! Now for the final actions!
     
    #action for display and save
    if [ "$action" = "$action1:$action2" ]
    then
            rm "$file".md5sum
            echo $sum > "$file".md5sum
            zenity --info --title="$title" --text "<b>$file:</b>
     
    $text4
    <b>$sum</b>
     
    $text5
    <b>$file.md5sum</b>"
            exit
    fi
     
    #action for display only
    if [ "$action" = "$action1" ]
    then
            zenity --info --title="$title" --text "<b>$file:</b>
     
    $text4
    <b>$sum</b>"
            exit
    fi
     
    #action for save only
    if [ "$action" = "$action2" ]
    then
            rm "$file".md5sum
            echo $sum > "$file".md5sum
            zenity --info --title="$title" --text "<b>$file:</b>
     
    $text5
    <b>$file.md5sum</b>"
            exit
    fi
    killall md5sum
    exit

