#!/usr/bin/env ruby
input = ARGV[0]
regex = /\[from:(?<sender>[^\]]+)\].*\[to:(?<receiver>[^\]]+)\].*\[flags:(?<flags>[^\]]+)\]/
match = input.match(regex)

if match
  puts "#{match[:sender]},#{match[:receiver]},#{match[:flags]}"
else
  puts ""
end
