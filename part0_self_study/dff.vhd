library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity dff is
  port (
    clk : in std_logic;
    reset_n : in std_logic;
    d : in std_logic;
    q : out std_logic
  );
end entity dff;

architecture rtl of dff is
  signal q_int : std_logic := '0';
begin
  process(clk)
  begin
    if rising_edge(clk) then
      if reset_n = '0' then
        q_int <= '0';
      else
        q_int <= d;
      end if;
    end if;
  end process;

  q <= q_int;

end architecture rtl;