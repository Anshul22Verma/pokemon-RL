local socket = require("socket")

local server = assert(socket.bind("127.0.0.1", 9999))

server:settimeout(0)

print("Waiting for Python connection...")

local client = nil

while client == nil do
    client = server:accept()
end

print("Python connected!")

client:settimeout(0)

while true do

    local command = client:receive()

    if command ~= nil then

        joypad.set({
            A = false,
            B = false,
            Up = false,
            Down = false,
            Left = false,
            Right = false
        })

        if command == "A" then
            joypad.set({A=true})

        elseif command == "B" then
            joypad.set({B=true})

        elseif command == "UP" then
            joypad.set({Up=true})

        elseif command == "DOWN" then
            joypad.set({Down=true})

        elseif command == "LEFT" then
            joypad.set({Left=true})

        elseif command == "RIGHT" then
            joypad.set({Right=true})
        end
    end

    local frame = gui.gdscreenshot()

    client:send(frame)

    emu.frameadvance()
end