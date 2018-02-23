class openssh {
	if $::operatingsystem == 'RedHat' {
		$package = 'httpd'
			$service = 'httpd'
				$path = '/root/dir/ntp.conf'
				}
					elsif $::operatingsystem == 'Centos' {
						$package = 'ntp'
							$service = 'ntpd'
								$path = '/root/dir/dir5/ntp.conf'
								}
								else {
									notify {"This $::operatingsystem is not supported" :}
									}	
										package {"$package":
											ensure => 'latest',
											}
												service {"$service":
													ensure => 'running',
														enable => 'true',
															require => Package ["$package"],
															}
																define openssh (
																	$mika,
																		$baiysh,
																			$baxa,
																				$template = 'openssh/ntpd.conf.erb'
																				){
																					file {"$title":
																						ensure => file,
																							content => template("$template"),	
																							}
																							}#define
																									openssh {"$path" :
																											mirka => ["Mickey Bekov", "Puppet engineer", "lead engineer"],
																													baxa => "Bakyt Abdishov",
																															baiysh => "Baiysh Talas",
																																	require => Package ["$package"],
																																			subscribe => Service ["$service"],
																																			}
																																			}#class

