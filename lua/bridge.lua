local input_file = "input.txt"
local img_file = "frame.png"

while true do

    -- read action
    local file = io.open(input_file, "r")
    local action = "NONE"

    if file then
        action = file:read("*all")
        file:close()
    end

    action = string.gsub(action, "%s+", "")

    joypad.set({})

    if action == "A" then joypad.set({A=true})
    elseif action == "B" then joypad.set({B=true})
    elseif action == "UP" then joypad.set({Up=true})
    elseif action == "DOWN" then joypad.set({Down=true})
    elseif action == "LEFT" then joypad.set({Left=true})
    elseif action == "RIGHT" then joypad.set({Right=true})
    end

    emu.frameadvance()

    -- THIS ALWAYS WORKS
    client.screenshot(img_file)
end