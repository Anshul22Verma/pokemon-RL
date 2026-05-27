local input_file = "input.txt"
local frame_file = "frame.raw"

while true do

    -- Read action from Python
    local file = io.open(input_file, "r")
    local action = "NONE"

    if file then
        action = file:read("*all")
        file:close()
    end

    action = string.gsub(action, "%s+", "")

    -- Reset input
    joypad.set({
        A=false, B=false,
        Up=false, Down=false,
        Left=false, Right=false
    })

    if action == "A" then joypad.set({A=true})
    elseif action == "B" then joypad.set({B=true})
    elseif action == "UP" then joypad.set({Up=true})
    elseif action == "DOWN" then joypad.set({Down=true})
    elseif action == "LEFT" then joypad.set({Left=true})
    elseif action == "RIGHT" then joypad.set({Right=true})
    end

    emu.frameadvance()

    -- ⭐ THIS is the correct screenshot API in BizHawk
    local img = client.get_screen_buffer()

    local f = io.open(frame_file, "wb")
    if f then
        f:write(img)
        f:close()
    end
end