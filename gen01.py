input_file = "google-domains.txt"
output_file = "adguard-allowlist.txt"

def convert_to_adguard_allowlist(input_file, output_file):
    allowlist = []

    with open(input_file, "r", encoding="utf-8") as infile:
        for line in infile:
            line = line.strip()

            # Skip comments and empty lines
            if not line or line.startswith("#"):
                continue

            if line.startswith("0.0.0.0"):
                parts = line.split()
                if len(parts) > 1:
                    domain = parts[1]
                    # Strip wildcard prefix or invalid domain characters
                    domain = domain.lstrip("*-")
                    allowlist.append(f"@@||{domain}^")

    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write("\n".join(allowlist))

    print(f"Converted {len(allowlist)} domains to AdGuard allowlist: {output_file}")

convert_to_adguard_allowlist(input_file, output_file)
